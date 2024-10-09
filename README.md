# bind-rpz
Create Bind response policy zones from Adblock filter standard

## Usage

<ol>
	<li>Configration</li>

Edit "ret_noerror" to change bind dns return => '0' for a NXDOMAIN return or '1' for a NOERROR.<br>
You can also edit the SRC url list in the 'links' variable
 
<li> Generate the policy zone</li>

python3 bind-rpz.py

<li>Add in your bind configuration options (Generally /etc/bind/named.conf.options)</li>

options {
response-policy { zone "banlist"; };
}

<li>Add a zone where "file" path link to the generate file in step 2</li>

zone "banlist" {
	type master;
	file "/etc/bind/db.banlist";
	allow-query {none;};
 };
 
</ol>
