<h1>About</h1>
This is a simple python script that was developed for a homelab server, that is port forwared through an ISP that doesn't offer a static IP address. Since the homelab server doesn't run 24/7, it just runs once when it is started. It creates a file, and saves the IP there. If it detects that the IP has been changed, it uses Twillo to send an Whatsapp Message, notifying you that the IP has changed. 

<h1>Getting a Twillo Account</h1>

<h1>Installing</h1>
<h2>Prequisities</h2>
<ul>
<li>Public IP Python Library
<ul>
`pip install publicip`
</ul>
</li>
<li>Requests Library
<ul>
`pip install requests`
</ul></li>
<li>Twillo Library
<ul>
`pip install twillo`
</ul></li>

</ul>