TurnKey Oracle XE 11g
==================================================

This is `Oracle Database 11g Express Edition
<http://www.oracle.com/technetwork/products/express-edition/overview/index.html>`_
`virtual appliance <http://en.wikipedia.org/wiki/Virtual_appliance>`_. A
virtual appliance is a virtual machine image designed to run on a
virtualization platform.

The appliance is based on `TurnKey Core <http://www.turnkeylinux.org/core>`_
that provides a small footprint Linux server tailored for virtual appliance
use. The appliance doesn't include Oracle XE out of the box because of unclear
licensing issue but provides a ready-made environment where the installation
of Oracle is easy to do by following these instructions.

The instructions are targetted to `VirtualBox <https://www.virtualbox.org/>`_
installation as it's the only virtualization environment were I have run the
appliance so far.

The high level steps are:

1. set up a VirtualBox virtual machine (or any other virtualization platform)
2. log in to virtual machine and install and configure Oracle

Resources
--------------------------------------------------

- `Oracle Database 11g Express Edition <http://www.oracle.com/technetwork/products/express-edition/overview/index.html>`_
- `Oracle Database Express Edition 11g Release 2 download page <http://www.oracle.com/technetwork/products/express-edition/downloads/index.html>`_
- `Oracle Database Express Edition Installation Guide for Linux x86-64 <http://docs.oracle.com/cd/E17781_01/install.112/e18802/toc.htm>`_
- `Ask Ubuntu <http://askubuntu.com>`_: `How to install Oracle Express 11gR2? <http://askubuntu.com/questions/198163/how-to-install-oracle-express-11gr2>`_
- `Installing Oracle 11g R2 Express Edition on Ubuntu 64-bit <http://meandmyubuntulinux.blogspot.fi/2012/05/installing-oracle-11g-r2-express.html>`_
- `Oracle 11g AMM: MEMORY_TARGET, MEMORY_MAX_TARGET and /dev/shm <http://blog.oracle48.nl/oracle-11g-amm-memory_target-memory_max_target-and-dev_shm/>`_
- `VirtualBox <https://www.virtualbox.org/>`_

VirtualBox Setup
--------------------------------------------------

If you don't know yet how to setup VirtualBox please check TurnKey's `Appliance
installation tutorial with VirtualBox
<http://www.turnkeylinux.org/docs/installation-appliances-virtualbox>`_.

Set the following appliance specific values when creating a new VirtualBox
virtual machine:

- Memory: 2GB

- Disk size: 21GB (there will be 16GB free space after installation)

- Network adapter: Bridged

If you need more disk space just increase the disk size as much as you like.

2GB memory is probably too much as according to Oracle documents XE uses 1 GB
at maximum. But OTOH 2GB RAM creates 2045MB swap that fullfills Oracle swap
requirement.

How to install Oracle XE
--------------------------------------------------

First get the zipped Oracle XE RPM package from `Oracle site <http://www.oracle.com/technetwork/products/express-edition/downloads/index.html>`_ and upload it to
a virtual machine.

Downloading the package requires an account to Oracle site and accepting a license.
 
Log in to the virtual machine as root and run the following commands:

0. Unzip:

::

    unzip oracle-xe-11.2.0-1.0.x86_64.rpm.zip

1. Convert RPM to a debian package:

::

    alien --scripts Disk1/oracle-xe-11.2.0-1.0.x86_64.rpm

2. Install:

::

    dpkg --install oracle-xe_11.2.0-2_amd64.deb

3. Run some other modifications needed by Oracle:

::

    /etc/init.d/shm_load start

4. Configure Oracle:

::

    /etc/init.d/oracle-xe configure responseFile=oracle.rsp >> oracle-install.log

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

Create an Oracle user account:

::

    root@turnkey-oracle-xe-11g ~# $ORACLE_HOME/bin/sqlplus sys/<PASSWORD> as
    sysdba @bin/mkorauser.sql <USERNAME> <PASSWORD>
