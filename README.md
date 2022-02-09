# Veterinerlik Uygulaması

## Kullandıklarım

+ Ben projeyi Pycharm IDE'sinde hazırladım. Fakat IDE olmadan da çalıştırılabilir olmasına özen gösterdim.
+ Requirements dosyasını da ekledim. Kullandığım paketlerin listesi orada.
+ Veritabanı olarak bir şey belirtilmediği için *Postgresql* kullanmayı tercih ettim.
+ Önyüzünde Bootstrap kullandım. (Yine de biraz hızlı hazırlamaya gayret ettiğim için önyüzsel görünüm kötülükleri olabilir.)
+ Django-admin paneli kullandım.


## Login-Register Aşaması

+ Kayıt aşamasını django-allauth ile otomatik yapmak istedim fakat modelleri o paketten alsam da viewleri kendim yazdım.
+ Uygulamaya ilk girildiğinde login isteyecek şekilde tasarladım o ekrandan kayıt ekranına da yönlendirme verdim. Eğer login işlemi yapıldıysa hayvanların listelendiği ekrana yönlendirdim. Login işlemi yapılmadığı takdirde bu ekranı görünüme kapalı bıraktım.


## İçerik
+ Aynı kullanıcıya birden fazla hayvan tanımlanabilir şekilde tasarladım animal_detay sayfasında her hayvan sahibinin sahip olduğu tüm hayvanları listeledim.
+ Listeden kayıt silme her kaydın yanında mevcut.
+ İletişim bilgileri için ayrı bir model oluşturdum. User modeline yeni field'lar ekleyerek yapmak istemiştim fakat hızlandırmak adına bu şekilde yaptım.
