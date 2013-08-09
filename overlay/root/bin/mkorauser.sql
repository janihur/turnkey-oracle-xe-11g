/* Create a database user

Usage:

$ sqlplus @mkorauser.sql sys/<PASSWORD> as sysdba <USERNAME> <PASSWORD>
*/

define p_username=&&1
define p_password=&&2

/* Default profile password limits

select resource_name, limit from dba_profiles where profile = 'DEFAULT';
alter profile DEFAULT limit password_life_time 365;
alter profile DEFAULT limit password_grace_time 30;
select username, profile, account_status, lock_date, expiry_date from dba_users;

*/

create user &&p_username identified by &&password;

alter user &&p_username default tablespace users temporary tablespace temp;

grant create session to &&p_username;
grant unlimited tablespace to &&p_username;
grant create table to &&p_username;
grant create sequence to &&p_username;

grant create procedure to &&p_username;

grant create database link to &&p_username;
grant create public database link to &&p_username;

grant create view to &&p_username;

grant create type to &&p_username;
grant create synonym to &&p_username;

/* Data pump */
grant read, write on directory data_pump_dir to &&p_username;

grant create trigger to &&p_username;
