#!/usr/bin/python
"""Set Oracle XE SYS-user password for silent installation

Option:
--dbpass= unless provided, will ask interactively
"""

import sys
import getopt

#import bcrypt

from dialog_wrapper import Dialog
#from executil import ExecError, system

def usage(s=None):
    if s:
        print >> sys.stderr, "Error:", s
    print >> sys.stderr, "Syntax: %s [options]" % sys.argv[0]
    print >> sys.stderr, __doc__
    sys.exit(1)

def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'dbpass='])
    except getopt.GetoptError, e:
        usage(e)

    dbpassword = ""
    
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--dbpass':
            dbpassword = val

    if not dbpassword:
        d = Dialog('TurnKey Linux - First boot configuration')
        dbpassword = d.get_password(
            "Oracle XE SYS Password",
            "Enter new password for the Oracle XE SYS-user.")

    # if not email:
    #     if 'd' not in locals():
    #         d = Dialog('TurnKey Linux - First boot configuration')

    #     email = d.get_email(
    #         "GitLab Email",
    #         "Enter email address for the GitLab 'admin' account.",
    #         "admin@example.com")

    # if not domain:
    #     if 'd' not in locals():
    #         d = Dialog('TurnKey Linux - First boot configuration')

    #     domain = d.get_input(
    #         "GitLab Domain",
    #         "Enter the domain to serve GitLab.",
    #         DEFAULT_DOMAIN)

    # if domain == "DEFAULT":
    #     domain = DEFAULT_DOMAIN

    #%(dbpassword)s
    with open("/root/oracle.rsp", "w") as text_file:
        text_file.write("""###############################################################################
#                                                                             #
# HTTP port that will be used to access APEX admin page                       #
# Default : 8080                                                              #
#                                                                             #
###############################################################################
ORACLE_HTTP_PORT=8080

###############################################################################
#                                                                             #
# TNS port that will be used to configure listener                            #
# Default : 1521                                                              #
#                                                                             #
###############################################################################
ORACLE_LISTENER_PORT=1521

###############################################################################
#                                                                             #
# Passwords can be supplied for the following two schemas in the              #
# starter database:                                                           #
#   SYS                                                                       #
#   SYSTEM                                                                    #
#                                                                             #
###############################################################################
ORACLE_PASSWORD=%(dbpassword)s

###############################################################################
#                                                                             #
# Passwords can be supplied for the following two schemas in the              #
# starter database:                                                           #
#   SYS                                                                       #
#   SYSTEM                                                                    #
#                                                                             #
#   ORACLE_CONFIRM_PASSWORD should be same as ORACLE_PASSWORD                 #
#                                                                             #
###############################################################################
ORACLE_CONFIRM_PASSWORD=%(dbpassword)s

###############################################################################
#                                                                             #
# To start/stop listener and database instance up on system boot              #
#                                                                             #
###############################################################################
ORACLE_DBENABLE=y
""" % {'dbpassword': dbpassword})

    # salt = bcrypt.gensalt(10)
    # hash = bcrypt.hashpw(password, salt)

    # m = MySQL()
    # m.execute('UPDATE gitlab_production.users SET email=\"%s\" WHERE username=\"admin\";' % email)
    # m.execute('UPDATE gitlab_production.users SET encrypted_password=\"%s\" WHERE username=\"admin\";' % hash)

    # config = "/home/git/gitlab/config/gitlab.yml"
    # system("sed -i \"s|host:.*|host: %s|\" %s" % (domain, config))
    # system("sed -i \"s|email_from:.*|email_from: %s|\" %s" % (email, config))

    # system_github("git config --global user.email %s" % email)
    # system_github("bundle exec rake gitlab:env:info RAILS_ENV=production")

    # # restart gitlab if its running
    # try:
    #     system("/etc/init.d/gitlab status")
    #     system("/etc/init.d/gitlab restart")
    # except ExecError:
    #     pass

if __name__ == "__main__":
    main()
