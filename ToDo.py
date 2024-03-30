import datetime
import os, glob
tasklar = [ ]

def Ekle():
    task = input("Task gir: ")
    tasklar.append(task)
    print(f"\n '{task}' eklendi.\n Kaydetmeyi unutma.\n ")


##### folder okuma alanı 
def okuma():
    files = glob.glob('*.txt')
    if not files:
        print("\n Hiç kayıtlı task yok. ¯\_(ツ)_/¯ ")
        return

    for filename in glob.glob('*.txt'):
      with open(os.path.join(os.getcwd(), filename), 'r') as f: 
       print(filename, "Dosyasındaki task \n", f.read())
def kaydet():
    timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H-%M")
    dosyaadi = f"todo {timestamp}.txt"
    with open(dosyaadi, "w") as file:
        for task in tasklar:
            file.write(task)
    print(f"\n task {task} {dosyaadi} dosyasına kaydedildi. \n ")
    #### input girmeden enter basınca hata veriyo error handling gerekli


### load eklenecek / ASSIGN DENEME ALANI GEÇİCİ

def assign_numbers_to_txt_files():
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    
    for idx, txt_file in enumerate(txt_files, start=1):
        print(f"{idx}. {txt_file}")
    if not txt_files or not len(txt_files):
        print("\n Hiç kayıtlı task yok ¯\_(ツ)_/¯")
        return
    file_number = int(input("Düzenlemek istediğin dosya numarasını gir: "))
    
    if 1 <= file_number <= len(txt_files):
        selected_file = txt_files[file_number - 1]
        file_path = os.path.join(os.getcwd(), selected_file)
        
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"{selected_file} içindeki task listeleniyor: \n \/")
            print(f"-->   {content}   <--")
            
            new_content = input("eklemeni yap: ")
            
            with open(file_path, 'w') as file:
                new_content = content + "\n" + new_content
                file.write(new_content)
                print(f"\n {selected_file} güncellendi.")
    else:
        print("Böyle bi task yok. ^_^ ")
#### dosya silme eklenmeli     
def Sil():
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    
    for idx, txt_file in enumerate(txt_files, start=1):
        print(f"\n {idx}. {txt_file}")
    if len(txt_files) == 0:
        print("\n Zaten hiç kayıtlı task yok. ¯\_(ツ)_/¯ ")
        return    
    file_number = int(input("\n Silmek istediğin task numarasını gir \n (Kayıtlı olmayan tasklar gözükmez): "))
    if 1 <= file_number <= len(txt_files):
        selected_file = txt_files[file_number - 1]
        file_path = os.path.join(os.getcwd(), selected_file)
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"{selected_file} içindeki task listeleniyor: \n \/")
            print(f"-->   {content}   <--")
    new_content = input("silmek istiyor musun? y/n: ")
    if new_content == "y":
        os.remove(file_path)
        print(f" {selected_file} silindi.\n ")
    elif new_content == "n":
        print("\n Silme islemi iptal edildi. ")
        return
    else:
        print("\n Sadece 'y' ya da 'n' girmelisin. ^_^")
        return Sil()


#### load deneme alanı 


def listele():
   if not tasklar:
       print("\n Hiç aktif task yok. ¯\_(ツ)_/¯ ")
   else:
        print("aktif tasklar: \n ")
        for index, task in enumerate(tasklar):
            print(f"Task {index}. {task}") 
if __name__ == "__main__":
    # uygulamayi acmak icin gerekli loop ha bu 
    print(">>> To Do List <<<")
    while True:
        print(" \n Ne yapmak istersin? ")
        print("_____________________ \n")
        print("1. Task Ekle")
        print("2. Eklenen taskları kaydet")
        print("3. Task Sil")
        print("4. Aktif taskları Listele")
        print("5. Kayıtlı taskları listele")
        print("6. Bir taska ekleme yap")
        print("7. Çıkış")
        print("______________________")

        secim_yap = input("Yapmak istedigin islemi gir: ")

        if secim_yap == "1":
            Ekle()       
        elif secim_yap == "2":
            kaydet()
        elif secim_yap == "3":
            Sil()
        elif secim_yap == "4":
            listele()
        elif secim_yap == "5":
            okuma()
        elif secim_yap == "6":
            assign_numbers_to_txt_files()
        elif secim_yap == "7":
            break
        else:
            print("\n Yanlis giris yaptin. \n tekrar dene.")
    print('''
                    ==                     ==
                 <^\()/^>               <^\()/^>
                  \/  \/                 \/  \/
                   /__\      .  '  .      /__\ 
      ==            /\    .     |     .    /\            ==
   <^\()/^>       !_\/       '  |  '       \/_!       <^\()/^>
    \/  \/     !_/I_||  .  '   \'/   '  .  ||_I\_!     \/  \/
     /__\     /I_/| ||      -== + ==-      || |\_I\     /__/
     /_ \   !//|  | ||  '  .   /.\   .  '  || |  |\\!   /_ /
    (-   ) /I/ |  | ||       .  |  .       || |  | \I\ (=   )
     \__/!//|  |  | ||    '     |     '    || |  |  |\\!\__/
     /  \I/ |  |  | ||       '  .  '    *  || |  |  | \I/  /
    {_ __}  |  |  | ||    Yine bekleriz    || |  |  |  {____}
 _!__|= ||  |  |  | ||   *      +          || |  |  |  ||  |__!_
 _I__|  ||__|__|__|_||          A          ||_|__|__|__||- |__I_
 -|--|- ||--|--|--|-||       __/_\__  *    ||-|--|--|--||= |--|-
  |  |  ||  |  |  | ||      /\-'o'-/\      || |  |  |  ||  |  |
  |  |= ||  |  |  | ||     _||:<_>:||_     || |  |  |  ||= |  |
  |  |- ||  |  |  | || *  /\_/=====\_/\  * || |  |  |  ||= |  |
  |  |- ||  |  |  | ||  __|:_:_[I]_:_:|__  || |  |  |  ||- |  | 
 _|__|  ||__|__|__|_||:::::::::::::::::::::||_|__|__|__||  |__|_
 -|--|= ||--|--|--|-||:::::::::::::::::::::||-|--|--|--||- |--|-
  jgs|- ||  |  |  | ||:::::::::::::::::::::|| |  |  |  ||= |  | 
     ''')
    ### bunu yazan tosun