import tkinter as tk
from tkinter import *
from tkinter import messagebox
from xlwt import Workbook
import socket
from Bio import Entrez
from Bio import Medline
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import os
import requests
import http.client
import time
import urllib


win=tk.Tk()
win.title("Scholar.ly")
#win.geometry("800x500")
win.resizable(False,False)
window_height = 500
window_width = 800
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def show1():
    messagebox.showinfo("Info","This tool is developed by Debapratim Gupta in June 2019 as a part of Summer Internship Project at Center for Bioinformatics.\n\n Under the guidance/supervision of :\n Dr.V.Amouda and Mrs.G.Jeyakodi\n\n DEBAPRATIM GUPTA\n M.C.A.(2018-21)\n Department of Computer Science\n PONDICHERRY UNIVERSITY, INDIA")


def show2():
    messagebox.showinfo("Requirements","1. Uninterrupted Internet/LAN connection\n\n2. A system with WINDOWS Operating system\n\n3. 8 GB RAM (minimum)\n\n4. A system having C:\ drive")

def show3():
    messagebox.showinfo("Description","This is a tool designed to download all download-able \nfull free-text articles from PUBMED.\nHowever, if the full free-article is not available then the abstract is downloaded.")
menubar=Menu(win)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Admin", command=show1)
helpmenu.add_command(label="Requirements",command=show2)
menubar.add_cascade(label="Help", menu=helpmenu)
aboutmenu = Menu(menubar,tearoff=0)
aboutmenu.add_command(label="Description",command=show3)
menubar.add_cascade(label="About",menu=aboutmenu)
win.config(menu=menubar)

frame1=tk.Frame(win,bg="white",width=700,height=120)
frame1.pack(fill=tk.X,padx=0,pady=0)
logo = tk.PhotoImage(file="logo2.png")
label1=tk.Label(frame1,image=logo,bg="white",width=120,height=120)
label1.pack(side=tk.LEFT)
label2=tk.Label(frame1,bg="white",text="Centre for Bioinformatics",font=("Bookman Old Style",14,"bold"),fg="blue")
label2.place(x=128,y=30)
label3=tk.Label(frame1,bg="white",text="PONDICHERRY UNIVERSITY",font=("Times New Roman",10,"bold"),fg="black")
label3.place(x=159,y=60)
label4=tk.Label(frame1,bg="white",text="Scholar.ly",font=("Harrington",32,"bold"),fg="#FF4500")
label4.place(x=420,y=25)
frame2=tk.Frame(win,bg="white",width=700,height=380)
frame2.pack(fill=tk.X,padx=0,pady=0)
bioinfo=tk.PhotoImage(file="bioinfo.png")
label7=tk.Label(frame2,image=bioinfo,width=700,height=380)
label7.pack(fill=tk.X,padx=0,pady=0)
search=tk.PhotoImage(file="search.png")
label5=tk.Label(frame2,image=search,width=30,height=30)
label5.place(x=190,y=136)
label8=tk.Label(frame2,bg="white",text="...",fg="white",height=4,width=120,font=("Britannic Bold",10))
label8.place(x=0,y=320)
text_bar=tk.Text(frame2,relief=RIDGE,width=30,height=1,borderwidth=6,font=("Lucida Handwriting", 9))
#text_bar.insert(tk.END, "Search keywords...")
text_bar.place(x=225,y=140)

label6=tk.Label(frame2,bg="white",text="Downloading..",height=2,width=12,fg="white")
label6.place(x=525,y=160)



def download():
    i=0
    k = 0
    z = 0
    try:
     term=text_bar.get("1.0",END+"-1c")
     Entrez.email = 'debexam1234@gmail.com'
     h1 = Entrez.esearch(db='pubmed', term=term)
     result2 = Entrez.read(h1)

     max_count = 1
     j = 0
     count= result2['Count']
    except RuntimeError:
     win.withdraw()
     messagebox.showerror("Error","Sorry! Could not Download.\n Please enter relevant keyword(s).")
     sys.exit()
    except (urllib.error.URLError, http.client.IncompleteRead, socket.gaierror):
        messagebox.showerror("Error", "Error occurred.Check internet connection and restart.")
        sys.exit()
    print('Total number of publications containing {0}: {1}'.format(term, count))

    start = 0
    c = int(count, 10)
    if c == 0:
        messagebox.showerror("Error","No Articles found. Search with other keyword(s).")
        start=1
    else:
        label6.configure(bg="yellow", text="Downloading...",fg="black")
        messagebox.showwarning("CAUTION","Download in progress.. Please do not terminate the process\n\n Note: Your articles will be downloaded in C:\ drive \n\with Folder name Research_Articles\n\nPress OK")
    wb1 = Workbook()
    sheet1 = wb1.add_sheet("Sheet 1",cell_overwrite_ok=True)
    sheet1.write(0, 0, "PMID")
    sheet1.write(0,1,"File Type")
    sheet1.write(0,2,"Title")
    while start <= c:
     try:
        h = Entrez.esearch(db='pubmed', retmax=max_count, retstart=start, term=term, sort='relevance')
        result = Entrez.read(h)
        print('Getting available full text articles/journals publications containing {0}...'.format(term))

        ids = result['IdList']
        h = Entrez.efetch(db='pubmed', id=ids, rettype='Medline', retmode='text')

        records = Medline.parse(h)
        column = 3
        for record in records:
            try:
                print("entered..")
                j = j + 1
                arr = record.get('PMID', '?')
                if arr == '?':
                    print("no id")
                    continue
                print(j, "PMID : ", arr)
                from pubmed_lookup import PubMedLookup

                # NCBI will contact user by email if excessive queries are detected
                email = 'debexam1234@gmail.com'
                url = 'http://www.ncbi.nlm.nih.gov/pubmed/' + str(arr)
                print(url)
                lookup = PubMedLookup(url, email)
                from pubmed_lookup import Publication
                publication = Publication(lookup)
                ff = 0
                print('attempting to download')

                folder_location2 = r'C:\Research_Articles'
                if not os.path.exists(folder_location2):
                    os.mkdir(folder_location2)
                file_location = os.path.join(folder_location2, term)
                if not os.path.exists(file_location):
                    os.mkdir(file_location)


                response2 = requests.get(url, timeout=120)
                soup = BeautifulSoup(response2.text, "html.parser")
                for link in soup.select('a[href*="pdf"]'):
                    # Name the pdf files using the last portion of each link which are unique in this case
                    print('Fetching research articles...')
                    filename = os.path.join(file_location, link['href'].split('/')[-1])
                    if '.pdf' not in filename:
                        filename += '.pdf'
                    with open(filename, "wb") as f:
                        f.write(requests.get(urljoin(url, link['href']), timeout=120).content)
                        print(filename, '    SUCESSFULLY saved !!')
                        sheet1.write(j,0,arr)
                        sheet1.write(j,1,"PDF")
                        sheet1.write(j,2,str(publication.title))
                        sheet1.write(j,column,str(filename))
                        ff=1
                    column=column+1
                    wb1.save(file_location+"\\"+term+".xls")

                print("Redirected to Publication URL : ", publication.url)
                if publication.url:
                    print('attempting to download')
                    url2 = publication.url
                    # If there is no such folder, the script will create one automatically
                    folder_location = r'C:\Research_Articles'
                    if not os.path.exists(folder_location):
                        os.mkdir(folder_location)
                    file_location = os.path.join(folder_location, term)
                    if not os.path.exists(file_location):
                        os.mkdir(file_location)

                    #sheet1 = wb1.add_sheet("Sheet 1")
                    wb1.save(file_location + "\\" + term + ".xls")
                    #sheet1.write(0, 0, "PMID")
                    response = requests.get(url2, timeout=120)
                    soup = BeautifulSoup(response.text, "html.parser")
                    for link in soup.select('a[href*="pdf"]'):
                        # Name the pdf files using the last portion of each link which are unique in this case
                        print('Fetching research articles...')

                        timeout = time.time() + 60 * 5
                        filename = os.path.join(file_location, link['href'].split('/')[-1])
                        if not (filename.endswith('.pdf')):
                            filename += '.pdf'
                        with open(filename, "wb") as f:
                            try:
                                f.write(requests.get(urljoin(url2, link['href']), timeout=120).content)
                            except Exception:
                                print("Some Error occurred")
                                pass
                            print(filename, '    SUCESSFULLY saved !!')
                            sheet1.write(j, 0, arr)
                            sheet1.write(j, 1, "PDF")
                            sheet1.write(j, 2, str(publication.title))
                            sheet1.write(j, column, str(filename))
                            ff = 2
                        column = column + 1
                        wb1.save(file_location + "\\" + term + ".xls")
                        if time.time() > timeout:
                            continue
                if ff == 0:
                    # print("Full text not found. So we try to save the abstract..")
                    path = r'C:\Research_Articles'
                    if not os.path.exists(path):
                        os.mkdir(path)
                    file_location = os.path.join(path, term)
                    if not os.path.exists(file_location):
                        os.mkdir(file_location)
                    i = i + 1
                    new_file_location = os.path.join(file_location, "Abstract" + str(i) + ".txt")
                    file1 = open(new_file_location, "w", encoding="utf-8")
                    title = str(publication.title)
                    author = str(publication.authors)
                    journal = str(publication.journal)
                    day = str(publication.day)
                    month = str(publication.month)
                    year = str(publication.year)
                    citation = str(publication.cite())
                    abstract = str(repr(publication.abstract))
                    to_file1 = title + '\n' + author + '\n' + journal + '\n' + day + '.' + month + '.' + year + '\n' + citation + '\n' + abstract
                    try:
                        file1.write(to_file1)
                    except Exception:
                        print("Some Error occurred")
                        pass
                    print("Abstract is saved..")
                    file1.close()
                    sheet1.write(j, 0, arr)
                    sheet1.write(j, 1, "TEXT")
                    sheet1.write(j, 2, str(publication.title))
                    sheet1.write(j,column, str(new_file_location))
                    column = column + 1
                    wb1.save(file_location + "\\" + term + ".xls")
            # except(ConnectionResetError, ConnectionAbortedError, requests.exceptions.SSLError, TypeError,OSError, ValueError, ConnectionError, http.client.HTTPException, urllib3.exceptions.ProtocolError,http.client.RemoteDisconnected, requests.exceptions.ConnectionError, http.client.IncompleteRead, requests.exceptions.ChunkedEncodingError):

            #except (urllib.error.URLError,http.client.IncompleteRead):
                #messagebox.showerror("Error","Error occurred.Check internet connection and restart.")
                #exit(0)


            except Exception as e:
                #messagebox.showerror("Network Error", "SORRY. Cannot download 1 file(s).\n\n Press OK to continue..")
                print("Error occured ....>>")
                pass

            finally:
                print("exited..")
                pass
        start = start + 1
     except (urllib.error.URLError,http.client.IncompleteRead,socket.error,socket.gaierror,socket.timeout):
         messagebox.showerror("Error", "RETRY.\n\nCHECK INTERNET CONNECTION.")
         sys.exit()

     if c!=0 and start>c:
        dir = "C:\\Research_Articles\\" + str(term)
        for file in os.listdir(dir):
            if file.endswith(".pdf"):
                k = k + 1
            if file.endswith(".txt"):
                z = z + 1
        label8.configure(text="No.of PDFs downloaded : " + str(k) + "\n\nNo.of Abstracts downloaded : " + str(z),bg="green")
        label6.configure(bg="green", text="Downloaded!", fg="white", height=2, width=12)
        messagebox.showinfo("CONGRATS !!","Your articles/abstracts have been downloaded successfully.\nAnd saved in C:\ drive.")
        time.sleep(3)
        sys.exit()


def rdownload():
    i = 0
    k = 0
    z = 0
    try:
        term = text_bar.get("1.0", END + "-1c")
        Entrez.email = 'debexam1234@gmail.com'
        h1 = Entrez.esearch(db='pubmed', term=term)
        result2 = Entrez.read(h1)

        max_count = 1
        j = 0
        count = result2['Count']
    except RuntimeError:
        win.withdraw()
        messagebox.showerror("Error", "Sorry! Could not Download.\n Please enter relevant keyword(s).")
        sys.exit()
    except (urllib.error.URLError, http.client.IncompleteRead, socket.gaierror):
        messagebox.showerror("Error", "Error occurred.Check internet connection and restart.")
        sys.exit()
    print('Total number of publications containing {0}: {1}'.format(term, count))

    start = 0
    c = 30
    if c == 0:
        messagebox.showerror("Error", "No Articles found. Search with other keyword(s).")
        start = 1
    else:
        label6.configure(bg="yellow", text="Downloading...", fg="black")
        messagebox.showwarning("CAUTION",
                               "Download in progress.. Please do not terminate the process\n\n Note: Your articles will be downloaded in C:\ drive \n\with Folder name Research_Articles\n\nPress OK")
    wb1 = Workbook()
    sheet1 = wb1.add_sheet("Sheet 1", cell_overwrite_ok=True)
    sheet1.write(0, 0, "PMID")
    sheet1.write(0, 1, "File Type")
    sheet1.write(0, 2, "Title")
    while start <= c:
        try:
            h = Entrez.esearch(db='pubmed', retmax=max_count, retstart=start, term=term, sort='most recent')
            result = Entrez.read(h)
            print('Getting available full text articles/journals publications containing {0}...'.format(term))

            ids = result['IdList']
            h = Entrez.efetch(db='pubmed', id=ids, rettype='Medline', retmode='text')

            records = Medline.parse(h)
            column = 3
            for record in records:
                try:
                    print("entered..")
                    j = j + 1
                    arr = record.get('PMID', '?')
                    if arr == '?':
                        print("no id")
                        continue
                    print(j, "PMID : ", arr)
                    from pubmed_lookup import PubMedLookup

                    # NCBI will contact user by email if excessive queries are detected
                    email = 'debexam1234@gmail.com'
                    url = 'http://www.ncbi.nlm.nih.gov/pubmed/' + str(arr)
                    print(url)
                    lookup = PubMedLookup(url, email)
                    from pubmed_lookup import Publication
                    publication = Publication(lookup)
                    ff = 0
                    print('attempting to download')

                    folder_location2 = r'C:\Recent_Research_Articles'
                    if not os.path.exists(folder_location2):
                        os.mkdir(folder_location2)
                    file_location = os.path.join(folder_location2, term)
                    if not os.path.exists(file_location):
                        os.mkdir(file_location)

                    response2 = requests.get(url, timeout=120)
                    soup = BeautifulSoup(response2.text, "html.parser")
                    for link in soup.select('a[href*="pdf"]'):
                        # Name the pdf files using the last portion of each link which are unique in this case
                        print('Fetching research articles...')
                        filename = os.path.join(file_location, link['href'].split('/')[-1])
                        if '.pdf' not in filename:
                            filename += '.pdf'
                        with open(filename, "wb") as f:
                            f.write(requests.get(urljoin(url, link['href']), timeout=120).content)
                            print(filename, '    SUCESSFULLY saved !!')
                            sheet1.write(j, 0, arr)
                            sheet1.write(j, 1, "PDF")
                            sheet1.write(j, 2, str(publication.title))
                            sheet1.write(j, column, str(filename))
                            ff = 1
                        column = column + 1
                        wb1.save(file_location + "\\" + term + ".xls")

                    publication = Publication(lookup)
                    print("Redirected to Publication URL : ", publication.url)
                    if publication.url:
                        print('attempting to download')
                        url2 = publication.url
                        # If there is no such folder, the script will create one automatically
                        folder_location = r'C:\Recent_Research_Articles'
                        if not os.path.exists(folder_location):
                            os.mkdir(folder_location)
                        file_location = os.path.join(folder_location, term)
                        if not os.path.exists(file_location):
                            os.mkdir(file_location)

                        # sheet1 = wb1.add_sheet("Sheet 1")
                        wb1.save(file_location + "\\" + term + ".xls")
                        # sheet1.write(0, 0, "PMID")
                        response = requests.get(url2, timeout=120)
                        soup = BeautifulSoup(response.text, "html.parser")
                        for link in soup.select('a[href*="pdf"]'):
                            # Name the pdf files using the last portion of each link which are unique in this case
                            print('Fetching research articles...')

                            timeout = time.time() + 60 * 5
                            filename = os.path.join(file_location, link['href'].split('/')[-1])
                            if not (filename.endswith('.pdf')):
                                filename += '.pdf'
                            with open(filename, "wb") as f:
                                try:
                                    f.write(requests.get(urljoin(url2, link['href']), timeout=120).content)
                                except Exception:
                                    print("Some Error occurred")
                                    pass
                                print(filename, '    SUCESSFULLY saved !!')
                                sheet1.write(j, 0, arr)
                                sheet1.write(j, 1, "PDF")
                                sheet1.write(j, 2, str(publication.title))
                                sheet1.write(j, column, str(filename))
                                ff = 2
                            column = column + 1
                            wb1.save(file_location + "\\" + term + ".xls")
                            if time.time() > timeout:
                                continue
                    if ff == 0:
                        # print("Full text not found. So we try to save the abstract..")
                        path = r'C:\Recent_Research_Articles'
                        if not os.path.exists(path):
                            os.mkdir(path)
                        file_location = os.path.join(path, term)
                        if not os.path.exists(file_location):
                            os.mkdir(file_location)
                        i = i + 1
                        new_file_location = os.path.join(file_location, "Abstract" + str(i) + ".txt")
                        file1 = open(new_file_location, "w", encoding="utf-8")
                        title = str(publication.title)
                        author = str(publication.authors)
                        journal = str(publication.journal)
                        day = str(publication.day)
                        month = str(publication.month)
                        year = str(publication.year)
                        citation = str(publication.cite())
                        abstract = str(repr(publication.abstract))
                        to_file1 = title + '\n' + author + '\n' + journal + '\n' + day + '.' + month + '.' + year + '\n' + citation + '\n' + abstract
                        try:
                            file1.write(to_file1)
                        except Exception:
                            print("Some Error occurred")
                            pass
                        print("Abstract is saved..")
                        file1.close()
                        sheet1.write(j, 0, arr)
                        sheet1.write(j, 1, "TEXT")
                        sheet1.write(j, 2, str(publication.title))
                        sheet1.write(j, column, new_file_location)
                        column = column + 1
                        wb1.save(file_location + "\\" + term + ".xls")
                # except(ConnectionResetError, ConnectionAbortedError, requests.exceptions.SSLError, TypeError,OSError, ValueError, ConnectionError, http.client.HTTPException, urllib3.exceptions.ProtocolError,http.client.RemoteDisconnected, requests.exceptions.ConnectionError, http.client.IncompleteRead, requests.exceptions.ChunkedEncodingError):

                # except (urllib.error.URLError,http.client.IncompleteRead):
                # messagebox.showerror("Error","Error occurred.Check internet connection and restart.")
                # exit(0)

                except Exception:
                    #messagebox.showerror("Network Error",
                                        # "SORRY. Cannot download 1 file(s).\n\n Press OK to continue..")
                    print("Error occured ....>>")
                    pass

                finally:
                    print("exited..")
                    pass
            start = start + 1
        except (urllib.error.URLError, http.client.IncompleteRead, socket.error, socket.gaierror, socket.timeout):
            messagebox.showerror("Error", "RETRY.\n\nCHECK INTERNET CONNECTION.")
            sys.exit()

    if c != 0 and start > c:
        dir = "C:\\Recent_Research_Articles\\" + str(term)
        for file in os.listdir(dir):
            if file.endswith(".pdf"):
                k = k + 1
            if file.endswith(".txt"):
                z = z + 1
        label8.configure(text="No.of PDFs downloaded : " + str(k) + "\n\nNo.of Abstracts downloaded : " + str(z),
                         bg="green")
        label6.configure(bg="green", text="Downloaded!", fg="white", height=2, width=12)
        messagebox.showinfo("CONGRATS !!",
                            "Your articles/abstracts have been downloaded successfully.\nAnd saved in C:\ drive.")
        time.sleep(3)
        sys.exit()

button1=tk.Button(frame2,bg="green",text="DOWNLOAD ARTICLES / ABSTRACTS",fg="white",font=("Arial",10,"bold"),command=download)
button1.place(x=225,y=180)
button2=tk.Button(frame2,bg="#808000",text="DOWNLOAD RECENT ARTICLES / ABSTRACTS",fg="white",font=("Arial",10,"bold"),command=rdownload)
button2.place(x=190,y=220)

win.mainloop()