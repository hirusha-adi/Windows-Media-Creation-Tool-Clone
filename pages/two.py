
import sys

import tkinter as tk
import tkinter.ttk as ttk
py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

import pages.three as third_page

def vp_start_gui_second():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Windows_11_Setup (root)
    init(root, top)
    root.mainloop()

w = None
def create_Windows_11_Setup(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Windows_11_Setup(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Windows_11_Setup (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Windows_11_Setup():
    global w
    w.destroy()
    w = None

class Windows_11_Setup:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("623x482+776+216")
        top.minsize(120, 1)
        top.maxsize(2948, 1261)
        top.resizable(1,  1)
        top.title("Widnows 11 Setup")
        top.configure(background="#ffffff")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.resizable(False, False)

        self.Topic_ONE = tk.Label(top)
        self.Topic_ONE.place(relx=0.032, rely=0.021, height=50, width=504)
        self.Topic_ONE.configure(activebackground="#f9f9f9")
        self.Topic_ONE.configure(activeforeground="black")
        self.Topic_ONE.configure(anchor='w')
        self.Topic_ONE.configure(background="#ffffff")
        self.Topic_ONE.configure(disabledforeground="#a3a3a3")
        self.Topic_ONE.configure(font="-family {Source Sans Pro} -size 24")
        self.Topic_ONE.configure(foreground="#31aed2")
        self.Topic_ONE.configure(highlightbackground="#d9d9d9")
        self.Topic_ONE.configure(highlightcolor="black")
        self.Topic_ONE.configure(text='''Applicable notices and license terms''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.ms_label = tk.Label(top)
        self.ms_label.place(relx=0.048, rely=0.919, height=30, width=74)
        self.ms_label.configure(activebackground="#f9f9f9")
        self.ms_label.configure(activeforeground="black")
        self.ms_label.configure(background="#ffffff")
        self.ms_label.configure(disabledforeground="#a3a3a3")
        self.ms_label.configure(font="-family {Source Sans Pro} -size 11 -weight bold")
        self.ms_label.configure(foreground="#6e6e6e")
        self.ms_label.configure(highlightbackground="#d9d9d9")
        self.ms_label.configure(highlightcolor="black")
        self.ms_label.configure(text='''Microsoft''')

        self.support_label = tk.Label(top)
        self.support_label.place(relx=0.177, rely=0.919, height=30, width=64)
        self.support_label.configure(activebackground="#f9f9f9")
        self.support_label.configure(activeforeground="black")
        self.support_label.configure(background="#ffffff")
        self.support_label.configure(disabledforeground="#a3a3a3")
        self.support_label.configure(font="-family {Source Sans Pro} -size 11")
        self.support_label.configure(foreground="#6e6e6e")
        self.support_label.configure(highlightbackground="#d9d9d9")
        self.support_label.configure(highlightcolor="black")
        self.support_label.configure(text='''Support''')

        self.legal_label = tk.Label(top)
        self.legal_label.place(relx=0.289, rely=0.919, height=30, width=44)
        self.legal_label.configure(activebackground="#f9f9f9")
        self.legal_label.configure(activeforeground="black")
        self.legal_label.configure(background="#ffffff")
        self.legal_label.configure(disabledforeground="#a3a3a3")
        self.legal_label.configure(font="-family {Source Sans Pro} -size 11")
        self.legal_label.configure(foreground="#6e6e6e")
        self.legal_label.configure(highlightbackground="#d9d9d9")
        self.legal_label.configure(highlightcolor="black")
        self.legal_label.configure(text='''Legal''')
        
        def exit_program():
            exit()

        def go_to_third_page():
            top.destroy()
            third_page.vp_start_gui_third()

        self.exit_btn = tk.Button(top)
        self.exit_btn.place(relx=0.69, rely=0.9, height=34, width=77)
        self.exit_btn.configure(activebackground="#ececec")
        self.exit_btn.configure(activeforeground="#000000")
        self.exit_btn.configure(background="#e0e0e0")
        self.exit_btn.configure(borderwidth="0")
        self.exit_btn.configure(disabledforeground="#a3a3a3")
        self.exit_btn.configure(foreground="#000000")
        self.exit_btn.configure(highlightbackground="#d9d9d9")
        self.exit_btn.configure(highlightcolor="black")
        self.exit_btn.configure(pady="0")
        self.exit_btn.configure(text='''Decline''')
        self.exit_btn.configure(command=exit_program)

        self.next_btn = tk.Button(top)
        self.next_btn.place(relx=0.835, rely=0.9, height=34, width=77)
        self.next_btn.configure(activebackground="#ececec")
        self.next_btn.configure(activeforeground="#000000")
        self.next_btn.configure(background="#e0e0e0")
        self.next_btn.configure(borderwidth="0")
        self.next_btn.configure(disabledforeground="#a3a3a3")
        self.next_btn.configure(foreground="#000000")
        self.next_btn.configure(highlightbackground="#d9d9d9")
        self.next_btn.configure(highlightcolor="black")
        self.next_btn.configure(pady="0")
        self.next_btn.configure(text='''Next''')
        self.next_btn.configure(command=go_to_third_page)

        self.Topic1_subpart = tk.Label(top)
        self.Topic1_subpart.place(relx=0.032, rely=0.124, height=31, width=324)
        self.Topic1_subpart.configure(activebackground="#f9f9f9")
        self.Topic1_subpart.configure(activeforeground="black")
        self.Topic1_subpart.configure(anchor='w')
        self.Topic1_subpart.configure(background="#ffffff")
        self.Topic1_subpart.configure(disabledforeground="#a3a3a3")
        self.Topic1_subpart.configure(font="-family {Source Sans Pro} -size 9")
        self.Topic1_subpart.configure(foreground="#000000")
        self.Topic1_subpart.configure(highlightbackground="#d9d9d9")
        self.Topic1_subpart.configure(highlightcolor="black")
        self.Topic1_subpart.configure(text='''Please read this so you know what you're agreeing to''')

        self.ScrolledTextArea = ScrolledText(top)
        self.ScrolledTextArea.place(relx=0.048, rely=0.207, relheight=0.674
                , relwidth=0.907)
        self.ScrolledTextArea.configure(background="white")
        self.ScrolledTextArea.configure(font="TkTextFont")
        self.ScrolledTextArea.configure(foreground="black")
        self.ScrolledTextArea.configure(highlightbackground="#d9d9d9")
        self.ScrolledTextArea.configure(highlightcolor="black")
        self.ScrolledTextArea.configure(insertbackground="black")
        self.ScrolledTextArea.configure(insertborderwidth="3")
        self.ScrolledTextArea.configure(selectbackground="blue")
        self.ScrolledTextArea.configure(selectforeground="white")
        self.ScrolledTextArea.configure(wrap="word")
        self.lisence_agreement_text = """MICROSOFT SOFTWARE LICENSE TERMS

WINDOWS OPERATING SYSTEM

IF YOU LIVE IN (OR IF YOUR PRINCIPAL PLACE OF BUSINESS IS IN) THE UNITED STATES, PLEASE READ THE BINDING ARBITRATION CLAUSE AND CLASS ACTION WAIVER IN SECTION 11. IT AFFECTS HOW DISPUTES ARE RESOLVED.

Thank you for choosing Microsoft!

Depending on how you obtained the Windows software, this is a license agreement between (i) you and the device manufacturer or software installer that distributes the software with your device; or (ii) you and Microsoft Corporation (or, based on where you live or, if a business, where your principal place of business is located, one of its affiliates) if you acquired the software from a retailer. Microsoft is the device manufacturer for devices produced by Microsoft or one of its affiliates, and Microsoft is the retailer if you acquired the software directly from Microsoft. Note that if you are a volume license customer, use of this software is subject to your volume license agreement rather than this agreement.

This agreement describes your rights and the conditions upon which you may use the Windows software. You should review the entire agreement, including any supplemental license terms that accompany the software and any linked terms, because all of the terms are important and together create this agreement that applies to you. You can review linked terms by pasting the (aka.ms/) link into a browser window.

By accepting this agreement or using the software, you agree to all of these terms, and consent to the transmission of certain information during activation and during your use of the software as per the privacy statement described in Section 3. If you do not accept and comply with these terms, you may not use the software or its features. You may contact the device manufacturer or installer, or your retailer if you purchased the software directly, to determine its return policy and return the software or device for a refund or credit under that policy. You must comply with that policy, which might require you to return the software with the entire device on which the software is installed for a refund or credit, if any.

1.      Overview.

a.      Applicability. This agreement applies to the Windows software that is preinstalled on your device, or acquired from a retailer and installed by you, the media on which you received the software (if any), any fonts, icons, images or sound files included with the software, and also any Microsoft updates, upgrades, supplements or services for the software, unless other terms come with them. It also applies to Windows apps developed by Microsoft that provide functionality such as mail, contacts, music and photos that are included with and are a part of Windows. If this agreement contains terms regarding a feature or service not available on your device, then those terms do not apply.

b.      Additional terms. Additional Microsoft and third-party terms may apply to your use of certain features, services and apps, depending on your device’s capabilities, how it is configured, and how you use it. Please be sure to read them.

(i)      Some Windows apps provide an access point to, or rely on, online services, and the use of those services is sometimes governed by separate terms and privacy policies, such as the Microsoft Services Agreement at (aka.ms/msa). You can view these terms and policies by looking at the service terms of use or the app’s settings, as applicable. The services may not be available in all regions.

(ii)     Microsoft, the device manufacturer or installer may include additional apps, which will be subject to separate license terms and privacy policies.

(iii)    The software includes Adobe Flash Player that is licensed under terms from Adobe Systems Incorporated at (aka.ms/adobeflash). Adobe and Flash are either registered trademarks or trademarks of Adobe Systems Incorporated in the United States and/or other countries.

(iv)    The software may include third-party programs that are licensed to you under this agreement, or under their own terms. License terms, notices and acknowledgements, if any, for the third-party programs can be viewed at (aka.ms/thirdpartynotices).

(v)     To the extent included with Windows, Word, Excel, PowerPoint and OneNote are licensed for your personal, non-commercial use, unless you have commercial use rights under a separate agreement.

2.      Installation and Use Rights.

a.      License. The software is licensed, not sold. Under this agreement, we grant you the right to install and run one instance of the software on your device (the licensed device), for use by one person at a time, so long as you comply with all the terms of this agreement. Updating or upgrading from non-genuine software with software from Microsoft or authorized sources does not make your original version or the updated/upgraded version genuine, and in that situation, you do not have a license to use the software.

b.      Device. In this agreement, “device” means a hardware system (whether physical or virtual) with an internal storage device capable of running the software. A hardware partition or blade is considered to be a device.

c.      Restrictions. The device manufacturer or installer and Microsoft reserve all rights (such as rights under intellectual property laws) not expressly granted in this agreement. For example, this license does not give you any right to, and you may not:

(i)      use or virtualize features of the software separately;

(ii)     publish, copy (other than the permitted backup copy), rent, lease, or lend the software;

(iii)    transfer the software (except as permitted by this agreement);

(iv)    work around any technical restrictions or limitations in the software;

(v)     use the software as server software, for commercial hosting, make the software available for simultaneous use by multiple users over a network, install the software on a server and allow users to access it remotely, or install the software on a device for use only by remote users;

(vi)    reverse engineer, decompile, or disassemble the software, or attempt to do so, except and only to the extent that the foregoing restriction is (a) permitted by applicable law; (b) permitted by licensing terms governing the use of open-source components that may be included with the software; or (c) required to debug changes to any libraries licensed under the GNU Lesser General Public License which are included with and linked to by the software; and

(vii)   when using Internet-based features you may not use those features in any way that could interfere with anyone else’s use of them, or to try to gain access to or use any service, data, account, or network, in an unauthorized manner.

d.      Multi use scenarios.

(i)      Multiple versions. If when acquiring the software you were provided with multiple versions (such as 32-bit and 64-bit versions), you may install and activate only one of those versions at a time.

(ii)     Multiple or pooled connections. Hardware or software you use to multiplex or pool connections, or reduce the number of devices or users that access or use the software, does not reduce the number of licenses you need. You may only use such hardware or software if you have a license for each instance of the software you are using.

(iii)    Device connections. You may allow up to 20 other devices to access the software installed on the licensed device for the purpose of using the following software features: file services, print services, Internet information services, and Internet connection sharing and telephony services on the licensed device. You may allow any number of devices to access the software on the licensed device to synchronize data between devices. This section does not mean, however, that you have the right to install the software, or use the primary function of the software (other than the features listed in this section), on any of these other devices.

(iv)    Use in a virtualized environment. This license allows you to install only one instance of the software for use on one device, whether that device is physical or virtual. If you want to use the software on more than one virtual device, you must obtain a separate license for each instance.

(v)     Remote access. No more than once every 90 days, you may designate a single user who physically uses the licensed device as the licensed user. The licensed user may access the licensed device from another device using remote access technologies. Other users, at different times, may access the licensed device from another device using remote access technologies, but only on devices separately licensed to run the same or higher edition of this software.

(vi)    Remote assistance. You may use remote assistance technologies to share an active session without obtaining any additional licenses for the software. Remote assistance allows one user to connect directly to another user’s computer, usually to correct problems.

e.      Backup copy. You may make a single copy of the software for backup purposes, and may also use that backup copy to transfer the software if it was acquired as stand-alone software, as described in Section 4 below.

3.      Privacy; Consent to Use of Data. Your privacy is important to us. Some of the software features send or receive information when using those features. Many of these features can be switched off in the user interface, or you can choose not to use them. By accepting this agreement and using the software you agree that Microsoft may collect, use, and disclose the information as described in the Microsoft Privacy Statement (aka.ms/privacy), and as may be described in the user interface associated with the software features.

4.      Transfer. The provisions of this section do not apply if you acquired the software in Germany or in any of the countries listed on this site (aka.ms/transfer), in which case any transfer of the software to a third party, and the right to use it, must comply with applicable law.

a.      Software preinstalled on device. If you acquired the software preinstalled on a device (and also if you upgraded from software preinstalled on a device), you may transfer the license to use the software directly to another user, only with the licensed device. The transfer must include the software and, if provided with the device, an authentic Windows label including the product key. Before any permitted transfer, the other party must agree that this agreement applies to the transfer and use of the software.

b.      Stand-alone software. If you acquired the software as stand-alone software (and also if you upgraded from software you acquired as stand-alone software), you may transfer the software to another device that belongs to you. You may also transfer the software to a device owned by someone else if (i) you are the first licensed user of the software and (ii) the new user agrees to the terms of this agreement. You may use the backup copy we allow you to make or the media that the software came on to transfer the software. Every time you transfer the software to a new device, you must remove the software from the prior device. You may not transfer the software to share licenses between devices.

5.      Authorized Software and Activation. You are authorized to use this software only if you are properly licensed and the software has been properly activated with a genuine product key or by other authorized method. When you connect to the Internet while using the software, the software will automatically contact Microsoft or its affiliate to conduct activation to associate it with a certain device. You can also activate the software manually by Internet or telephone. In either case, transmission of certain information will occur, and Internet, telephone and SMS service charges may apply. During activation (or reactivation that may be triggered by changes to your device’s components), the software may determine that the installed instance of the software is counterfeit, improperly licensed or includes unauthorized changes. If activation fails, the software will attempt to repair itself by replacing any tampered Microsoft software with genuine Microsoft software. You may also receive reminders to obtain a proper license for the software. Successful activation does not confirm that the software is genuine or properly licensed. You may not bypass or circumvent activation. To help determine if your software is genuine and whether you are properly licensed, see (aka.ms/genuine). Certain updates, support, and other services might only be offered to users of genuine Microsoft software.

6.      Updates. The softwareperiodically checks for system and app updates, and downloads and installs them for you. You may obtain updates only from Microsoft or authorized sources, and Microsoft may need to update your system to provide you with those updates. By accepting this agreement, you agree to receive these types of automatic updates without any additional notice.

7.      Downgrade Rights. If you acquired a device from a manufacturer or installer with a Professional version of Windows preinstalled on it and it is configured to run in full feature mode, you may use either a Windows 8.1 Pro or Windows 7 Professional version, but only for so long as Microsoft provides support for that earlier version as set forth in (aka.ms/windowslifecycle). This agreement applies to your use of the earlier versions. If the earlier version includes different components, any terms for those components in the agreement that comes with the earlier version apply to your use of such components. Neither the device manufacturer or installer, nor Microsoft, is obligated to supply earlier versions to you. You must obtain the earlier version separately, for which you may be charged a fee. At any time, you may replace an earlier version with the version you originally acquired.

8.      Export Restrictions. You must comply with all domestic and international export laws and regulations that apply to the software, which include restrictions on destinations, end users, and end use. For further information on export restrictions, visit  (aka.ms/exporting).

9.      Warranty, Disclaimer, Remedy, Damages and Procedures.

a.      Limited Warranty. Depending on how you obtained the Windows software, Microsoft, or the device manufacturer or installer, warrants that properly licensed software will perform substantially as described in any Microsoft materials that accompany the software. This limited warranty does not cover problems that you cause, that arise when you fail to follow instructions, or that are caused by events beyond the reasonable control of Microsoft, or the device manufacturer or installer. The limited warranty starts when the first user acquires the software, and lasts for one year if acquired from Microsoft, or for 90 days if acquired from a device manufacturer or installer. If you obtain updates or supplements directly from Microsoft during the 90-day term of the device manufacturer’s or installer’s limited warranty, Microsoft provides the limited warranty for those updates or supplements. Any supplements, updates, or replacement software that you may receive from Microsoft during that year are also covered, but only for the remainder of that one-year period if acquired from Microsoft, or for 90 days if acquired from a device manufacturer or installer, or for 30 days, whichever is longer. Transferring the software will not extend the limited warranty.

b.      Disclaimer. Neither Microsoft, nor the device manufacturer or installer, gives any other express warranties, guarantees, or conditions. Microsoft and the devicemanufacturer and installerexclude all implied warranties and conditions, including those of merchantability, fitness for a particular purpose, and non-infringement. If your local law does not allow the exclusion of implied warranties, then any implied warranties, guarantees, or conditions last only during the term of the limited warranty and are limited as much as your local law allows. If your local law requires a longer limited warranty term, despite this agreement, then that longer term will apply, but you can recover only the remedies this agreement allows.

c.      Limited Remedy. If Microsoft, or the device manufacturer or installer, breaches its limited warranty, it will, at its election, either: (i) repair or replace the software at no charge, or (ii) accept return of the software (or at its election the device on which the software was preinstalled) for a refund of the amount paid, if any. The device manufacturer or installer (or Microsoft if you acquired them directly from Microsoft) may also repair or replace supplements, updates, and replacement of the software or provide a refund of the amount you paid for them, if any. These are your only remedies for breach of warranty. This limited warranty gives you specific legal rights, and you may also have other rights which vary from state to state or country to country.

d.      Damages. Except for any repair, replacement, or refund that Microsoft, or the device manufacturer or installer, may provide, you may not under this limited warranty, under any other part of this agreement, or under any theory, recover any damages or other remedy, including lost profits or direct, consequential, special, indirect, or incidental damages. The damage exclusions and remedy limitations in this agreement apply even if repair, replacement, or a refund does not fully compensate you for any losses, if Microsoft, or the device manufacturer or installer, knew or should have known about the possibility of the damages, or if the remedy fails of its essential purpose. Some states and countries do not allow the exclusion or limitation of incidental, consequential, or other damages, so those limitations or exclusions may not apply to you. If your local law allows you to recover damages from Microsoft, or the device manufacturer or installer, even though this agreement does not, you cannot recover more than you paid for the software (or up to $50 USD if you acquired the software for no charge).

e.      Warranty and Refund Procedures. For service or refund, you must provide a copy of your proof of purchase and comply with Microsoft’s return policies if you acquired the software from Microsoft, or the device manufacturer’s or installer’s return policies if you acquired the software from a device manufacturer or installer. If you purchased stand-alone software, those return policies might require you to uninstall the software and return it to Microsoft. If you acquired the software pre-installed on a device, those return policies may require return of the software with the entire device on which the software is installed; the certificate of authenticity label including the product key (if provided with your device) must remain affixed. Contact the device manufacturer or installer at the address or toll-free telephone number provided with your device to find out how to obtain warranty service for the software. If Microsoft is your device manufacturer or if you acquired the software from a retailer, contact Microsoft at:

(i)      United States and Canada. For warranty service or information about how to obtain a refund for software acquired in the United States or Canada, contact Microsoft via telephone at (800) MICROSOFT; via mail at Microsoft Customer Service and Support, One Microsoft Way, Redmond, WA 98052-6399; or visit (aka.ms/nareturns).

(ii)     Europe, Middle East, and Africa. If you acquired the software in Europe, the Middle East, or Africa, contact either Microsoft Ireland Operations Limited, Customer Care Centre, Atrium Building Block B, Carmanhall Road, Sandyford Industrial Estate, Dublin 18, Ireland, or the Microsoft affiliate serving your country (aka.ms/msoffices).

(iii)    Australia. If you acquired the software in Australia, contact Microsoft to make a claim at 13 20 58; or Microsoft Pty Ltd, 1 Epping Road, North Ryde NSW 2113 Australia.

(iv)    Other countries. If you acquired the software in another country, contact the Microsoft affiliate serving your country (aka.ms/msoffices).

10.    Support.

a.      For software preinstalled on a device. For the software generally, contact the device manufacturer or installer for support options. Refer to the support number provided with the software. For updates and supplements obtained directly from Microsoft, Microsoft may provide limited support services for properly licensed software as described at (aka.ms/mssupport).

b.      For software acquired from a retailer. Microsoft provides limited support services for properly licensed software as described at (aka.ms/mssupport).

11.    Binding Arbitration and Class Action Waiver if You Live in (or, if a Business, Your Principal Place of Business is in) the United States.

We hope we never have a dispute, but if we do, you and we agree to try for 60 days to resolve it informally. If we can’t, you and we agree to binding individual arbitration before the American Arbitration Association (“AAA”) under the Federal Arbitration Act (“FAA”), and not to sue in court in front of a judge or jury. Instead, a neutral arbitrator will decide and the arbitrator’s decision will be final except for a limited right of review under the FAA. Class action lawsuits, class-wide arbitrations, private attorney-general actions, and any other proceeding where someone acts in a representative capacity aren’t allowed. Nor is combining individual proceedings without the consent of all parties. “We,” “our,” and “us” includes Microsoft, the device manufacturer, and software installer.

a.      Disputes covered—everything except IP. The term “dispute” is as broad as it can be. It includes any claim or controversy between you and the device manufacturer or installer, or you and Microsoft, concerning the software, its price, or this agreement, under any legal theory including contract, warranty, tort, statute, or regulation, except disputes relating to the enforcement or validity of your, your licensors’, our, or our licensors’ intellectual property rights.

b.      Mail aNotice of Dispute first. If you have a dispute and our customer service representatives can’t resolve it, send a Notice of Dispute by U.S. Mail to the device manufacturer or installer, ATTN: LEGAL DEPARTMENT. If your dispute is with Microsoft, mail it to Microsoft Corporation, ATTN: CELA ARBITRATION, One Microsoft Way, Redmond, WA 98052-6399. Tell us your name, address, how to contact you, what the problem is, and what you want. A form is available at (aka.ms/disputeform). We’ll do the same if we have a dispute with you. After 60 days, you or we may start an arbitration if the dispute is unresolved.

c.      Small claims court option. Instead of mailing a Notice of Dispute, and if you meet the court’s requirements, you may sue us in small claims court in your county of residence (or, if a business, your principal place of business) or our principal place of business—King County, Washington USA if your dispute is with Microsoft.

d.      Arbitration procedure. The AAA will conduct any arbitration under its Commercial Arbitration Rules (or if you are an individual and use the software for personal or household use, or if the value of the dispute is $75,000 USD or less whether or not you are an individual or how you use the software, its Consumer Arbitration Rules). For more information, see (aka.ms/adr) or call 1-800-778-7879. To start an arbitration, submit the form available at (aka.ms/arbitration) to the AAA; mail a copy to the device manufacturer or installer (or to Microsoft if your dispute is with Microsoft). In a dispute involving $25,000 USD or less, any hearing will be telephonic unless the arbitrator finds good cause to hold an in-person hearing instead. Any in-person hearing will take place in your county of residence (or, if a business, your principal place of business) or our principal place of business—King County, Washington if your dispute is with Microsoft. You choose. The arbitrator may award the same damages to you individually as a court could. The arbitrator may award declaratory or injunctive relief only to you individually to satisfy your individual claim. Under AAA rules, the arbitrator rules on his or her own jurisdiction, including the arbitrability of any claim. But a court has exclusive authority to enforce the prohibition on arbitration on a class-wide basis or in a representative capacity.

e.      Arbitration fees and payments.

(i)      Disputes involving $75,000 USD or less. The device manufacturer or installer (or Microsoft if your dispute is with Microsoft) will promptly reimburse your filing fees and pay the AAA’s and arbitrator’s fees and expenses. If you reject our last written settlement offer made before the arbitrator was appointed, your dispute goes all the way to an arbitrator’s decision (called an “award”), and the arbitrator awards you more than this last written offer, the device manufacturer or installer (or Microsoft if your dispute is with Microsoft) will: (1) pay the greater of the award or $1,000 USD; (2) pay your reasonable attorney’s fees, if any; and (3) reimburse any expenses (including expert witness fees and costs) that your attorney reasonably accrues for investigating, preparing, and pursuing your claim in arbitration.

(ii)     Disputes involving more than $75,000 USD. The AAA rules will govern payment of filing fees and the AAA’s and arbitrator’s fees and expenses.

f.       Must file within one year. You and we must file in small claims court or arbitration any claim or dispute (except intellectual property disputes — see Section 11.a.) within one year from when it first could be filed. Otherwise, it’s permanently barred.

g.      Severability. If any part of Section 11 (Binding Arbitration and Class Action Waiver) is found to be illegal or unenforceable, the remainder will remain in effect (with an arbitration award issued before any court proceeding begins), except that if a finding of partial illegality or unenforceability would allow class-wide or representative arbitration, Section 11 will be unenforceable in its entirety.

h.      Conflict with AAA rules. This agreement governs if it conflicts with the AAA’s Commercial Arbitration Rules or Consumer Arbitration Rules.

i.       Microsoft as party or third-party beneficiary. If Microsoft is the device manufacturer or if you acquired the software from a retailer, Microsoft is a party to this agreement. Otherwise, Microsoft is not a party but is a third-party beneficiary of your agreement with the device manufacturer or installer to resolve disputes through informal negotiation and arbitration.

12.    Governing Law. The laws of the state or country where you live (or, if a business, where your principal place of business is located) govern all claims and disputes concerning the software, its price, or this agreement, including breach of contract claims and claims under consumer protection laws, unfair competition laws, implied warranty laws, for unjust enrichment, and in tort, regardless of conflict of law principles. In the United States, the FAA governs all provisions relating to arbitration.

13.    Consumer Rights, Regional Variations. This agreement describes certain legal rights. You may have other rights, including consumer rights, under the laws of your state or country. You may also have rights with respect to the party from which you acquired the software. This agreement does not change those other rights if the laws of your state or country do not permit it to do so. For example, if you acquired the software in one of the below regions, or mandatory country law applies, then the following provisions apply to you:

a.      Australia. References to “Limited Warranty” are references to the express warranty provided by Microsoft or the device manufacturer or installer. This warranty is given in addition to other rights and remedies you may have under law, including your rights and remedies under the Australian Consumer Law consumer guarantees. Nothing in this agreement limits or changes those rights and remedies. In particular:.

(i)      the provisions excluding and limiting warranties, guarantees, damages and remedies, and limiting duration of your rights under local laws in Section 9 headed Warranty, Disclaimer, Remedy, Damages and Procedures do not apply to the Australian Consumer Law consumer guarantees and your rights and remedies under them;

(ii)     support and refund policies referred to in Section 10 are subject to the Australian Consumer Law;

(iii)    the Australian Consumer Law consumer guarantees apply to the evaluation software described in Section 14 d (ii) and the preview software described in Section 14 d (iv); and

(iv)    our goods come with guarantees that cannot be excluded under the Australian Consumer Law. In this section, “goods” refers to the software for which Microsoft, the device manufacturer or installer provides the express warranty. You are entitled to a replacement or refund for a major failure and compensation for any other reasonably foreseeable loss or damage. You are also entitled to have the goods repaired or replaced if the goods fail to be of acceptable quality and the failure does not amount to a major failure.

To learn more about your rights under the Australian Consumer Law, please review the information at (aka.ms/acl).

b.      Canada. You may stop receiving updates on your device by turning off Internet access. If and when you re-connect to the Internet, the software will resume checking for and installing updates.

c.      European Union. The academic use restriction in Section 14.d(i) below does not apply in the jurisdictions listed on this site: (aka.ms/academicuse).

d.      Germany and Austria.

(i)      Warranty. The properly licensed software will perform substantially as described in any Microsoft materials that accompany the software. However, the device manufacturer or installer, and Microsoft, give no contractual guarantee in relation to the licensed software.

(ii)     Limitation of Liability. In case of intentional conduct, gross negligence, claims based on the Product Liability Act, as well as, in case of death or personal or physical injury, the device manufacturer or installer, or Microsoft is liable according to the statutory law.

Subject to the preceding sentence, the device manufacturer or installer, or Microsoft will only be liable for slight negligence if the device manufacturer or installer or Microsoft is in breach of such material contractual obligations, the fulfillment of which facilitate the due performance of this agreement, the breach of which would endanger the purpose of this agreement and the compliance with which a party may constantly trust in (so-called "cardinal obligations"). In other cases of slight negligence, the device manufacturer or installer or Microsoft will not be liable for slight negligence.

e.      Other regions. See (aka.ms/variations) for a current list of regional variations.

14.    Additional Notices.

a.      Networks, data and Internet usage. Some features of the software and services accessed through the software may require your device to access the Internet. Your access and usage (including charges) may be subject to the terms of your cellular or internet provider agreement. Certain features of the software may help you access the Internet more efficiently, but the software’s usage calculations may be different from your service provider’s measurements. You are always responsible for (i) understanding and complying with the terms of your own plans and agreements, and (ii) any issues arising from using or accessing networks, including public/open networks. You may use the software to connect to networks, and to share access information about those networks, only if you have permission to do so.

b.      H.264/AVC and MPEG-4 visual standards and VC-1 video standards. The software may include H.264/MPEG-4 AVC and/or VC-1 decoding technology. MPEG LA, L.L.C. requires this notice:

THIS PRODUCT IS LICENSED UNDER THE AVC, THE VC-1, AND THE MPEG-4 PART 2 VISUAL PATENT PORTFOLIO LICENSES FOR THE PERSONAL AND NON-COMMERCIAL USE OF A CONSUMER TO (i) ENCODE VIDEO IN COMPLIANCE WITH THE ABOVE STANDARDS (“VIDEO STANDARDS”) AND/OR (ii) DECODE AVC, VC-1, AND MPEG-4 PART 2 VIDEO THAT WAS ENCODED BY A CONSUMER ENGAGED IN A PERSONAL AND NON-COMMERCIAL ACTIVITY AND/OR WAS OBTAINED FROM A VIDEO PROVIDER LICENSED TO PROVIDE SUCH VIDEO. NO LICENSE IS GRANTED OR SHALL BE IMPLIED FOR ANY OTHER USE. ADDITIONAL INFORMATION MAY BE OBTAINED FROM MPEG LA, L.L.C. SEE (AKA.MS/MPEGLA).

c.      Malware protection. Microsoft cares about protecting your device from malware. The software will turn on malware protection if other protection is not installed or has expired. To do so, other antimalware software will be disabled or may have to be removed.

d.      Limited rightsversions. If the software version you acquired is marked or otherwise intended for a specific or limited use, then you may only use it as specified. You may not use such versions of the software for commercial, non-profit, or revenue-generating activities.

(i)      Academic. For academic use, you must be a student, faculty or staff of an educational institution at the time of purchase.

(ii)     Evaluation. For evaluation (or test or demonstration) use, you may not sell the software, use it in a live operating environment, or use it after the evaluation period. Notwithstanding anything to the contrary in this Agreement, evaluation software is provided “AS IS” and no warranty, implied or express (including the Limited Warranty), applies to these versions.

(iii)    NFR. You may not sell software marked as “NFR” or “Not for Resale”.

(iv)     Preview. You may choose to use preview, insider, beta, or other pre-release versions of the software (“previews”) that Microsoft may make available. You may use previews only up to the software’s expiration date and so long as you comply with all the terms of this agreement. Previews are experimental and may be substantially different from the commercially released version. Notwithstanding anything to the contrary in this agreement, previews are provided “AS IS,” and no warranty, implied or express (including the Limited Warranty), applies to these versions. By installing previews on your device, you may void or impact your device warranty and may not be entitled to support from your devicemanufacturer or network operator, if applicable. Microsoft is not responsible for any damage therebycaused to you. Microsoft may not provide support services for previews. If you provide Microsoft comments, suggestions or other feedback about the preview (“submission”), you grant Microsoft and its partners rights to use the submission in any way and for any purpose.

15.    Entire Agreement. This agreement (together with the printed paper license terms or other terms accompanying any software supplements, updates, and services that are provided by the device manufacturer or installer, or Microsoft, and that you use), and the terms contained in web links listed in this agreement, are the entire agreement for the software and any such supplements, updates, and services (unless the device manufacturer or installer, or Microsoft, provides other terms with such supplements, updates, or services). You can review this agreement after your software is running by going to (aka.ms/useterms) or going to Settings - System - About within the software. You can also review the terms at any of the links in this agreement by typing the URLs into a browser address bar, and you agree to do so. You agree that you will read the terms before using the software or services, including any linked terms. You understand that by using the software and services, you ratify this agreement and the linked terms. There are also informational links in this agreement. The links containing notices and binding terms are:

·        Microsoft Privacy Statement (aka.ms/privacy)

·        Microsoft Services Agreement (aka.ms/msa)

·        Adobe Flash Player License Terms (aka.ms/adobeflash)"""
        self.ScrolledTextArea.insert('end', self.lisence_agreement_text)
        self.ScrolledTextArea.configure(state='disabled')
# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

# if __name__ == '__main__':
#     vp_start_gui_second()




