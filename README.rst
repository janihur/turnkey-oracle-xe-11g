TurnKey Oracle XE 11g
=====================

Note: only a working draft !

Based on TurnKey Core. Doesn't include Oracle installation out of the box, but provides a simple environment where the installation of Orcale is easy to do it yourself.

HOw to install Orcale XE

Get the package from Oracle site.

convert RPM to debian package:
    alien --scripts oracle-xe-11.2.0-1.0.x86_64.rpm

Install:

    dpkg --install oracle-xe_11.2.0-2_amd64.deb

Run some stuff Orcale Needs:

    /etc/init.d/shm_load start

Configure: Oracle
/etc/init.d/oracle-xe configure

Now Orcale is running:

$ORACLE_HOME/bin/sqlplus sys/<PASSWORD> as sysdba
