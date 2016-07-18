#Amazon Web Services 
##Setting up Cloud Computing :cloud: :cloud: :cloud:

1.  Logging in  
  http://aws.amazon.com/  
  (Note:  put your user id and password somewhere for easy reference)

2.  [AWS Free Tier](https://aws.amazon.com/free/)  
  * credit card required for log-in
  * designed to enable you to get hands-on experience with AWS Cloud Services
  * includes services with a free tier available for 12 months following your AWS sign-up date, as well as additional service offers that do not automatically expire at the end of your 12 month AWS Free Tier term.

3.  AWS Console  
  Lot of options!  We will choose "Compute/EC2"  [upper left of screen]  
  EC2 = Elastic Compute Cloud (Virtual Servers in the Cloud!)  
  ![AWS Console](img/aws_console.png)

4.  Region [on upper right of screen]  
  Select:  US East (N. Virginia)

5.  Create Instance  
    From your EC2 Dashboard, click the blue **Launch Instance** button.

---
##Setting up Instance

Step 1) Choose an Amazon Machine Image (AMI):  **Ubuntu Server** [press blue Select button]  
Step 2) Choose an Instance Type:  Select a **Free tier eligible** "t2.micro" instance  
Step 3) **Next: Configure Instance Details**  [accept default]  
Step 4) **Next:  Add Storage**  [set to free max of 30GB]  
Step 5) Tag Instance: `awsds8`  
Step 6) **Next:  Configure Security Group**  
Name a new security group and allow some more ports if you like.  
>     Add Rule:  select 'Custom TCP Rule'  
      Port Range: 80  (for web REST)
      Source:  Anywhere  

**Review and Launch**    
    
Step 7) Review Instance Launch: your set-up will look like below screenshot  
**Launch**  

  ![review instance](img/aws_review_instance.png)
    
    
---

##Set up Secure Access  

1.  Choose to "Create a new key pair" and give it a name:  **aws_ds8key**  
2.  Download keypair

---

###Keypair
Save file.  For me, it is in this folder:  
```
julia$ pwd
/Users/julialintern/Downloads
julia$ 
julia$ ls -la *aws_ds8key*
-rw-r--r--@ 1   1692 Apr 23 14:46 aws_ds8key.pem
julia$ 
```  
Move your file to `~/.ssh/`.  (Note:  if you do not have an ssh folder, create one:  `mkdir ~/.ssh`)  
```  
julia$ mv aws_ds8key.pem ~/.ssh/aws_ds8key.pem 
```
Make your file read only with `chmod 400 filename`
```
julia$ cd ~/.ssh
julia$ pwd
/Users/julialintern/.ssh
julia$ ls -la *aws_ds8key*
-rw-r--r--@ 1   1692 Apr 23 14:46 aws_ds7key.pem

julia$ chmod 400 aws_ds8key.pem

julia$ ls -la *aws_ds8key*
-r--------@ 1   1692 Apr 23 14:46 aws_ds7key.pem
```  
Check that you have `id_rsa` and `id_rsa.pub` files within your .ssh file  
```
julia$ pwd
/Users/julialintern/.ssh
julia$ ls -la *id_rsa*
-rw-------  1   1675 Jun  2  2015 id_rsa
-rw-r--r--  1    422 Jun  2  2015 id_rsa.pub
```  
If you do not have them, generate them with `$ ssh-keygen -t rsa`    
(When asked where to save, the default location is correct (ex: /Users/username/.ssh/id_rsa) : so hit Enter)

--- 

##Connecting to your Instance  
###AWS:  
**Launch Instance**

##Set Up Billing  
Find (in blue):  "Get notified of estimated charges"  
Select **Create billing alerts**  
Check all 3 preferences and select **Save preferences**  
You can then close this tab.  
Back to other AWS tab.  Scroll down and select **View Instances**

On your EC2 Dashboard, you'll soon be able to find the IP address of your new cloud computer!  
**Note:  It may take a few minutes for the instance to initialize.**

###On Your Local Machine  

**Open a new terminal window.**

**My example:**  
####Generate ssh key  
```
reshama$ ssh-keygen -t rsa
reshama$
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/reshamashaikh/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/reshamashaikh/.ssh/id_rsa.
Your public key has been saved in /Users/reshamashaikh/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:X3a3M90WKnog8ONPmD5zd2dXQXYkPJDBvL+Xk4W8K2o reshamashaikh@RESHAMAs-MacBook-Pro.local
The key's randomart image is:
+---[RSA 2048]----+
|           oo=...|
|            + o+.|
|             .o..|
|     .      .  . |
|      o S   oo.oo|
|       +oo o .=.B|
|      .oo.o. . *O|
|      .+..Eoo.oB=|
|       .=++...+oo|
+----[SHA256]-----+
```

####(you can access it like this, if you are not in `.ssh` directory):  
**Note:  the numbers after "ubuntu@" come from AWS; it is the Public IP.**    
```
ssh -i ~/.ssh/my_key_file.pem ubuntu@123.234.123.234
```

####or if you are in the ssh directory  
```
reshama$ pwd
/Users/reshamashaikh/.ssh
```

####Connect to your Cloud Machine from your local computer!  
```
reshama$ ssh -i "aws_ds7key.pem" ubuntu@54.165.157.51  

The authenticity of host '54.165.157.51 (54.165.157.51)' can't be established.
ECDSA key fingerprint is SHA256:0/xYknp2uz/6NLgHjM8RRqpsX0ykIGj8xQV9PqL3mkU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '54.165.157.51' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-74-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Sat Apr 23 20:09:58 UTC 2016

  System load: 0.16             Memory usage: 5%   Processes:       82
  Usage of /:  9.9% of 7.74GB   Swap usage:   0%   Users logged in: 0

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ubuntu@ip-172-31-60-68:~$ 
```

####To exit Ubuntu machine (AWS cloud machine)  
```
ubuntu@ip-172-31-60-68:~$ exit
logout
Connection to 54.165.157.51 closed.
```





