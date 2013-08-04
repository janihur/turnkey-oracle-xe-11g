TurnKey Oracle XE 11g
==================================================

**Note that this is a working draft !**

The appliance is based on TurnKey Core. It doesn't include Oracle XE out of
the box yet but provides a ready-made environment where the installation of
Oracle is easy to do by following these instructions.

First set up a VirtualBox virtual machine and then log in and configure Oracle.

VirtualBox Setup
--------------------------------------------------

Set the following values when creating a new virtual machine:

- Memory: 2G

- Disk size: 21G (creates 2045MB swap and 15G free space after installation)

- Network adapter: bridged

If you need more disk space just increase the disk size as much as you'd like.

TODO: Memory and disk size could be in fact be a bit smaller, but the values
above work fine.

How to install Oracle XE
--------------------------------------------------

First get the zipped Oracle XE RPM package from Oracle site and upload it to
the virtual machine.

Downloading the package requires an account to Oracle site and accepting a license.
 
Log in to the virtual machine as root and run the following commands:

1. Convert RPM to a debian package:

::

    alien --scripts oracle-xe-11.2.0-1.0.x86_64.rpm

2. Install:

::

    dpkg --install oracle-xe_11.2.0-2_amd64.deb

3. Run some other modifications needed by Oracle:

::

    /etc/init.d/shm_load start

4. Configure Oracle:

::

    /etc/init.d/oracle-xe configure

The configuration script asks several question. You can accept the default
values for all other questions except to SYS-password.

That's it ! Now Oracle is running:

::

    root@turnkey-oracle-xe-11g ~# $ORACLE_HOME/bin/sqlplus sys/<PASSWORD> as sysdba
    
    SQL*Plus: Release 11.2.0.2.0 Production on Sun Aug 4 19:21:29 2013
    
    Copyright (c) 1982, 2011, Oracle.  All rights reserved.
    
    
    Connected to:
    Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
    
    SQL> select * from v$version;
    
    BANNER
    --------------------------------------------------------------------------------
    Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production
    PL/SQL Release 11.2.0.2.0 - Production
    CORE	11.2.0.2.0	Production
    TNS for Linux: Version 11.2.0.2.0 - Production
    NLSRTL Version 11.2.0.2.0 - Production
    
    SQL> 
