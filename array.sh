#!/bin/sh
#$ -S /bin/sh
#$ -t 1-7
#$ -o log/stdout.$JOB_ID.$TASK_ID
#$ -e log/stdout.$JOB_ID.$TASK_ID

task_1="./bash-auto1.sh"
task_2="./bash-auto2.sh"
task_3="./bash-auto3.sh"
task_4="./bash-auto4.sh"
task_5="./bash-auto5.sh"
task_6="./bash-auto6.sh"
task_7="./bash-auto7.sh"

eval \$task_$SGE_TASK_ID
