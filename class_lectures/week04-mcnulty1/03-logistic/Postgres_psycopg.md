### Connecting our Cloud Postgres DB within local ipynb..

1st
We will alter some configuration settings so that
we will be able to connect with our remote Postgres server locally (via python & pandas).

First, let's ssh into our cloud.. 

```bash
ssh ubuntu 

```

 We want to connect Postgres with SQL Alchemy and psycopg locally.  But first we'll just have to change a few settings.. 

```bash
sudo nano /etc/postgresql/9.3/main/postgresql.conf
```

On our postgresql.conf: change your
change listen_addresses='localhost' to listen_addresses='*'

```bash
sudo nano /etc/postgresql/9.3/main/pg_hba.conf
```

On our pg_hba.conf: let's add:
'host    all      all      65.209.60.146/0     trust'

(Save file and exit)

Restart server

```bash
sudo service postgresql restart
```


Now-- we will go to your LOCAL bash & install psycopg


```bash
conda install -c https://conda.binstar.org/alefnula psycopg2
```
