export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=$ORACLE_BASE/product/11.2.0/xe
export ORACLE_SID=XE

if [ -x $ORACLE_HOME/bin/nls_lang.sh ]; then
  export NLS_LANG=$($ORACLE_HOME/bin/nls_lang.sh)
fi

export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH
export PATH=$ORACLE_HOME/bin:$PATH

alias ll='ls -alF'
