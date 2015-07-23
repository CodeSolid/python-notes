
get_ipython().magic(u'ls ')
get_ipython().magic(u'cat log_all.py')
print ('session1')
quit()

print('session2')
get_ipython().magic(u'cat log_all.py')
log '--------------------------'
get_ipython().magic(u'cat log_all.py')
quit()

print('session with logstart off')
quit()

get_ipython().system(u'subl ../README.md')
get_ipython().magic(u'pwd ')
quit()

quit()

print('hi Jenniffer')
get_ipython().magic(u'cat log_all.py')
print('hi again')
get_ipython().magic(u'cat log_all.py')
quit()


get_ipython().magic(u"logstart 'delme.py'")
quit()

myfiles = get_ipython().getoutput(u'ls')
myfiles
quit()

myfiles = get_ipython().getoutput(u'ls')
myfiles.n
myfiles.p
myfiles.s
pyvar = 'hello world!'
get_ipython().system(u'echo "A python variable: {pyvar}"')
quit()



get_ipython().magic(u'run IPythonFriendlyMessage.py')
x = Message()
x = Message("Hello world")
x
get_ipython().magic(u'run IPythonFriendlyMessage.py')
x = Message("Hello world")
x
get_ipython().magic(u'cat log_all.py')
quit()

quit()


12/50
12.00 / 50.0
3.00 / 50.0
8.00 / 50.0
16.0 / 35.0
13.0 / 35.0
4.0 / 35.0
2.0 / 35.0
46+37+11+6
quit()

import pandas pd
import pandas as pd
pd.read_csv('birth_year_udacity.csv')
pd.read_csv('birth_year_udacity.csv')
tab = pd.read_csv('birth_year_udacity.csv')
tab.names
tab = pd.read_csv('birth_year_udacity.csv', names='names')
tab.names
tab = pd.read_csv('birth_year_udacity.csv', names=names)
tab = pd.read_csv('birth_year_udacity.csv', names='names')
tab
tab = pd.read_csv('birth_year_udacity.csv')
tab
tab.freq
tab.freq.sum()
get_ipython().system(u'subl log_all.py')
quit()

tab = read_csv('test_counts.csv')
import pandas as pd
pd.read_csv('test_counts.csv')
tab = pd.read_csv('test_counts.csv')
tab = pd.read_csv('test_counts.csv')
tab.names
tab['names']
tab('names')
tab = pd.read_csv('test_counts.csv', names='thenames'))
tab = pd.read_csv('test_counts.csv', names=thenames)
tab = pd.read_csv('test_counts.csv', names='thenames')
thenames
thenames['Names']
tab
tab = pd.read_csv('test_counts.csv')
tab
tab.Names
tab.Names.value_counts()
quit()


get_ipython().magic(u'edit value_counts.py')
get_ipython().magic(u'edit value_counts.py')
get_ipython().magic(u'run value_counts.py')
tab.Names.value_counts()
get_ipython().magic(u'run value_counts.py')
get_ipython().magic(u'run value_counts.py')
get_ipython().magic(u'pwd ')
get_ipython().magic(u'cd ../../')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd pydata-book/')
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ch02/')
get_ipython().magic(u'ls ')
quit()

import pandas as pd
z = pd.read_csv('names/yob1880.txt')
z
get_ipython().magic(u'cat names/yob1880.txt')
z = pd.read_csv('names/yob1880.txt', names=['name)
z = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'count')
)
z = pd.read_csv('names/yob1880.txt', names=['name', 'sex', 'count'])
z.name
z.sort(by=count)[:10]
z.sort(by='count')[:10]
z.sort('count')[:10]
z.sort('count', ascending=False)[:10]
y = pd.read_csv('names/yob1980.txt', names=['name', 'sex', 'count'])
y.sort('count', ascending=False)[:10]

import pandas as pd
events = pd.read_csv('pmi_events_smaller.csv')
events = pd.read_csv('pmi_events_smaller.csv', low_meory=False)
events = pd.read_csv('pmi_events_smaller.csv', low_memory=False)
events.names
names(events)
events.source
events._raw
events._raw.isin("Rs=IDC")
events._raw.isin(["Rs=IDC"])
events._raw.str.contains("Rs=IDC")
events[_raw[events._raw.str.contains("Rs=IDC")]
]
events[_raw[events._raw.str.contains("Rs=IDC")]]
events._raw[events._raw.str.contains("Rs=IDC")]
events[events._raw.str.contains("Rs=IDC")]
events._raw[events._raw.str.contains("Rs=IDC")]
events._raw[events._raw.str.contains("\*Rs=IDC")]
events._raw[events._raw.str.contains("\*Rs=IDC")]
events._raw[events._raw.str.contains("Rs=IDC")]
with_errors = events._raw[events._raw.str.contains("\Rs=IDC")]
pd.to_csv('errors')
with_errors.to_csv('pmi_errors')
with_errors = events._raw[events._raw.str.contains("\*Rs=PMI")]
with_errors.to_csv('pmi_errors')
quit()

get_ipython().magic(u'ls ')
import pandas as pd
big = pd.read_csv('march_12_to_13_pmi.json')
a = 10
_4
4__
_i4
_o4
_4
__i4
_i4
_4
foo = 'bar'
foo
_i14
_14
type(_14)
i = 9
i
type(_19)
type(_i19)
i_19
_i19
exit()

import pandas as pd;
pd.read_csv('pmi_events_smaller.csv')
pd.read_csv('pmi_events_smaller.csv', names='cols')
cols
pd.read_csv('pmi_events_smaller.csv', names=cols)
pd.read_csv('pmi_events_smaller.csv', names='cols')
pigstats.ScriptState - Pig features used in the script: UNKNOWN
2015-03-19 11:47:16,692 [main] INFO  org.apache.pig.newplan.logical.optimizer.LogicalPlanOptimizer - {RULES_ENABLED=[AddForEach, ColumnMapKeyPrune, GroupByConstParallelSetter, LimitOptimizer, LoadTypeCastInserter, MergeFilter, MergeForEach, NewPartitionFilterOptimizer, PartitionFilterOptimizer, PushDownForEachFlatten, PushUpFilter, SplitFilter, StreamTypeCastInserter], RULES_DISABLED=[FilterLogicExpressionSimplifier]}
2015-03-19 11:47:16,694 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MRCompiler - File concatenation threshold: 100 optimistic? false
2015-03-19 11:47:16,694 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MultiQueryOptimizer - MR plan size before optimization: 1
2015-03-19 11:47:16,694 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MultiQueryOptimizer - MR plan size after optimization: 1
2015-03-19 11:47:16,695 [main] INFO  org.apache.hadoop.metrics.jvm.JvmMetrics - Cannot initialize JVM Metrics with processName=JobTracker, sessionId= - already initialized
2015-03-19 11:47:16,696 [main] INFO  org.apache.pig.tools.pigstats.ScriptState - Pig script settings are added to the job
2015-03-19 11:47:16,696 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - mapred.job.reduce.markreset.buffer.percent is not set, set to default 0.3
2015-03-19 11:47:16,697 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - creating jar file Job5737832580292359363.jar
2015-03-19 11:47:18,567 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - jar file Job5737832580292359363.jar created
2015-03-19 11:47:18,573 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.JobControlCompiler - Setting up single store job
2015-03-19 11:47:18,579 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 1 map-reduce job(s) waiting for submission.
2015-03-19 11:47:18,582 [JobControl] INFO  org.apache.hadoop.metrics.jvm.JvmMetrics - Cannot initialize JVM Metrics with processName=JobTracker, sessionId= - already initialized
2015-03-19 11:47:18,583 [JobControl] ERROR org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl - Error while trying to run jobs.
java.lang.IncompatibleClassChangeError: Found interface org.apache.hadoop.mapreduce.JobContext, but class was expected
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.setupUdfEnvAndStores(PigOutputFormat.java:225)
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.checkOutputSpecs(PigOutputFormat.java:186)
at org.apache.hadoop.mapreduce.JobSubmitter.checkSpecs(JobSubmitter.java:562)
at org.apache.hadoop.mapreduce.JobSubmitter.submitJobInternal(JobSubmitter.java:432)
at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1296)
at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1293)
at java.security.AccessController.doPrivileged(Native Method)
at javax.security.auth.Subject.doAs(Subject.java:422)
at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1628)
at org.apache.hadoop.mapreduce.Job.submit(Job.java:1293)
at org.apache.hadoop.mapreduce.lib.jobcontrol.ControlledJob.submit(ControlledJob.java:335)
at org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl.run(JobControl.java:240)
at org.apache.pig.backend.hadoop20.PigJobControl.run(PigJobControl.java:121)
at java.lang.Thread.run(Thread.java:745)
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher$1.run(MapReduceLauncher.java:271)
2015-03-19 11:47:18,583 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 0% complete
2015-03-19 11:47:18,585 [main] WARN  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - Ooops! Some job has failed! Specify -stop_on_failure if you want Pig to stop immediately on failure.
2015-03-19 11:47:18,585 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - job null has failed! Stop running all dependent jobs
2015-03-19 11:47:18,585 [main] INFO  org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher - 100% complete
2015-03-19 11:47:18,598 [main] ERROR org.apache.pig.tools.pigstats.SimplePigStats - ERROR 2997: Unable to recreate exception from backend error: Unexpected System Error Occured: java.lang.IncompatibleClassChangeError: Found interface org.apache.hadoop.mapreduce.JobContext, but class was expected
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.setupUdfEnvAndStores(PigOutputFormat.java:225)
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.checkOutputSpecs(PigOutputFormat.java:186)
at org.apache.hadoop.mapreduce.JobSubmitter.checkSpecs(JobSubmitter.java:562)
at org.apache.hadoop.mapreduce.JobSubmitter.submitJobInternal(JobSubmitter.java:432)
at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1296)
at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1293)
at java.security.AccessController.doPrivileged(Native Method)
at javax.security.auth.Subject.doAs(Subject.java:422)
at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1628)
at org.apache.hadoop.mapreduce.Job.submit(Job.java:1293)
at org.apache.hadoop.mapreduce.lib.jobcontrol.ControlledJob.submit(ControlledJob.java:335)
at org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl.run(JobControl.java:240)
at org.apache.pig.backend.hadoop20.PigJobControl.run(PigJobControl.java:121)
at java.lang.Thread.run(Thread.java:745)
at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher$1.run(MapReduceLauncher.java:271)
2015-03-19 11:47:18,598 [main] ERROR org.apache.pig.tools.pigstats.PigStatsUtil - 1 map reduce job(s) failed!
2015-03-19 11:47:18,598 [main] INFO  org.apache.pig.tools.pigstats.SimplePigStats - Script Statistics: 
    
HadoopVersionPigVersionUserIdStartedAtFinishedAtFeatures
2.6.00.12.2-SNAPSHOTjohnlo2015-03-19 11:47:162015-03-19 11:47:18UNKNOWN
Failed!
Failed Jobs:
    JobIdAliasFeatureMessageOutputs
    N/AstuffMAP_ONLYMessage: Unexpected System Error Occured: java.lang.IncompatibleClassChangeError: Found interface org.apache.hadoop.mapreduce.JobContext, but class was expected
    	at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.setupUdfEnvAndStores(PigOutputFormat.java:225)
    	at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.PigOutputFormat.checkOutputSpecs(PigOutputFormat.java:186)
    	at org.apache.hadoop.mapreduce.JobSubmitter.checkSpecs(JobSubmitter.java:562)
    	at org.apache.hadoop.mapreduce.JobSubmitter.submitJobInternal(JobSubmitter.java:432)
    	at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1296)
    	at org.apache.hadoop.mapreduce.Job$10.run(Job.java:1293)
    	at java.security.AccessController.doPrivileged(Native Method)
    	at javax.security.auth.Subject.doAs(Subject.java:422)
    	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1628)
    	at org.apache.hadoop.mapreduce.Job.submit(Job.java:1293)
    	at org.apache.hadoop.mapreduce.lib.jobcontrol.ControlledJob.submit(ControlledJob.java:335)
    	at org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl.run(JobControl.java:240)
    	at org.apache.pig.backend.hadoop20.PigJobControl.run(PigJobControl.java:121)
    	at java.lang.Thread.run(Thread.java:745)
    	at org.apache.pig.backend.hadoop.executionengine.mapReduceLayer.MapReduceLauncher$1.run(MapReduceLauncher.java:271)
    

get_ipython().magic(u'ls ')
import pandas as pd
x = pd.read_csv('pmi_events_smaller.csv')
x = pd.read_csv('pmi_events_smaller.csv', low_memory=False)
x
x["_raw"]
x[20]
x.ix[20]
x.ix[15]
x.ix
x.ix.names
x.ix.ndim
x.index.get_loc("_raw")
x.index.get_loc(ds)
x[1]
x['_raw']
x['_raw'][0]
x['_raw'](0)
x['_raw']
quit()

import pandas as pd
data = pd.read_csv('pmi_new_query.csv')
data.names
data['_raw']
type(data)
raw = data['_raw']
type(raw0
)
type (raw)
test1 = re.compile("\*Rs=(.*)\|")
import re
test1 = re.compile("\*Rs=(.*)\|")
regex = test1
test1 = "foopdewop"
regex.match(test1)
result = regex.match(test1)
result
dump(result)
DUMP(result)
type(result)
test = "foobar etc*Rs=9999|mooger"
result = regex.match(test1)
result = regex.match(test)
type(result)
regex = re.compile("\*Rs\=(.*)\|")
result = regex.match(test)
type(result)
regex = re.compile("\*Rs\=.*")
type(result)
result = regex.match(test)
type(result)
regex = re.compile("Rs")
result = regex.match(test)
type(result)
regex = re.compile('Rs')
test
type(regex.match(test))
regex
type(regex)
test
test='foobarRs=99'
type(regex.match(test))
type(regex.match(test))
test='foobarRs=99'
regex = re.compile('.*Rs.*')
type(regex.match(test))
regex = re.compile('.*Rs=(.*)\.*')
type(regex.match(test))
match = regex.match(test)
match
match.groups
match.regs
test='foobarRs=99|'
match = regex.match(test)
match.regs
regex = re.compile('.*Rs=(.*)\|.*')
match = regex.match(test)
match.regs
regex = re.compile('.*Rs=(.*)\|')
match = regex.match(test)
match.regs
regex = re.compile('Rs=(.*)\|')
match = regex.match(test)
match.regs
regex = re.compile('.*Rs=(.*)\|')
test
test = '123Rs=99999|aaaaaaa'
regex = re.compile('.*Rs=(.*)\|')
match.regs
match = regex.match(test)
match.regs
test
test(6,11)
test[6,11]
test.find(match.regs[1])
match.
match.lastgroup
match.lastgroup()
match.regs
match.gropus
foo = match.group(1)
foo
quit()

get_ipython().magic(u'run run find_response.py')
get_ipython().magic(u'run find_response.py')
get_ipython().magic(u'run find_response.py')
s = get_response_string("aadsfalsdkjRs=99|asdlfjalsdkfj")
get_ipython().magic(u'run find_response.py')
s = get_response_string("aadsfalsdkjRs=99|asdlfjalsdkfj")
s
s = get_response_string("aadsfalsdkj**Rs=0000|asdlfjalsdkfj")
s
s = get_response_string("aadsfalsdkj**|asdlfjalsdkfj")
s
get_ipython().magic(u'edit find_response.py')
import find_response.py
get_ipython().magic(u'run find_response.py')
type(__get_response_string_regex)
s = get_response_string("aadsfalsdkj**Rs=0000|asdlfjalsdkfj")
s
import find_response
reload(find_response)
quit()

import find_response as fr
import pandas as pd
get_ipython().magic(u'ls ')
get_ipython().magic(u'cd ~/source/hadoop/')
get_ipython().magic(u'ls ')
data = pd.read_csv('pmi_new_query.csv')
data
data['new'] = 1
data
data2 = data['_raw']
data2
data3 = fr.get_response_string(data2['_raw'])
data3 = fr.get_response_string(data1['_raw'])
data3 = fr.get_response_string(data['_raw'])
data['raw']
data['_raw']
data['result'] = fr.get_response_string(data['_raw'])
data apply(lambda row: row['result'] = fr.get_response_string(row['_raw'])
)
data.apply(lambda row: row['result'] = fr.get_response_string(row['_raw'])
)
data['result'] = (fr.get_response_string(data['_raw']))
get_ipython().magic(u'pwd ')
get_ipython().magic(u'ls /Users/johnlo/Dropbox/science/python/ipython/')
get_ipython().magic(u'cp /Users/johnlo/Dropbox/science/python/ipython/find_response.py')
get_ipython().magic(u'cp /Users/johnlo/Dropbox/science/python/ipython/find_response.py .')
get_ipython().magic(u'ls ')
get_ipython().magic(u'edit find_response.py')
data
import find_response.py as fr
import find_response as fr
reload fr
reload find_response
reload find_response.py
reload find_response.py
pd
data
reload(find_response.py)
reload(find_response)
reload(fr)
data.apply(fr.get_column, axis=1)
data
newdata = data.apply(fr.get_column, axis=1)
newdata
data
data['response']
newdata = data.apply(fr.get_column, axis=1, raw=True)
data
x = [for index, row in data.iterrows() yield fr.get_response_string(row["_raw")]

cç
x = [for index, row in data.iterrows() yield fr.get_response_string(row["_raw"])]

cç
x = [for index, row in data.iterrows(): yield fr.get_response_string(row["_raw"])]

cç
x = [for index, row in data.iterrows() fr.get_response_string(row["_raw"])]

cç
x = [fr.get_response_string(row["_raw"]) for index, row in data.iterrows())
x = [fr.get_response_string(row["_raw"]) for index, row in data.iterrows()]
x
x = [fr.get_response_string(row["_raw"]) for row in data.iterrows()]
for x, row in data.iterrows:
    print(row['_raw'])
    
data
for (x, row) in data.iterrows:
    print(row['_raw'])
    
for (x, row) in data.iterrows():
    print(row['_raw'])
    
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
import find_response as fr
reload(find_response)
reload(fr)
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
reload(find_response)
import find_response as fr
reload(find_response)
reload(fr)
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
data['_raw']
import find_response as fr
reload(fr)
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
import find_response as fr
reload(fr)
import find_response as fr
for (x, row) in data.iterrows():
    print(fr.get_response_string(row['_raw']))
    
short = data.limit(20)
short = data[:10]
short
short = data[:20]
for (x, row) in short.iterrows():
    print(fr.get_response_string(row['_raw']))
    
short
for (x, row) in short.iterrows():
    print(fr.get_response_string(row['_raw']))
    
for (x, row) in short.iterrows():
    print(fr.get_response_string(row['_raw']))
    
data[:1]["_raw"]
data[:2]["_raw"]
data[:1]["_raw"]
x =data[:1]["_raw"]
x
type(x)
x =data[:1]["_raw"][0]
x
fr.get_response_string(x)
get_ipython().magic(u'paste')
def get_response(response_column):
	response = ''
	match = __get_response_string_regex.match(response_column)
	if (match):
		response = match.group(1)
	return response
def get_response(response_column):
    	response = ''
    	match = __get_response_string_regex.match(response_column)
    	if (match):
        		response = match.group(1)
        	return response
    
get_ipython().magic(u'cpaste')
def get_response(response_column):
	response = ''
	match = __get_response_string_regex.match(response_column)
	if (match):
		response = match.group(1)
	return response
get_response(x)
def get_response(response_column):
    	response = ''
    	match = __get_response_string_regex.match(response_column)
    	if (match):
        		response = match.group(1)
        	return response
    
import re
get_ipython().magic(u'pinfo re.match')
match = re.match(.*Rs\=(.*)\|',x)
match = re.match(".*Rs\=(.*)\|',x)
match = re.match(".*Rs\=(.*)\|",x)
match.group(1)
match = re.match(".*Rs\=(.*)\\|",x)
match.group(1)
match.lastgroup()
match.lastgroup
match.lastgroup()
match
match.lastgroup
match
match.regs
match = re.match(".*Rs\=(?P<result>.*)\\|",x)
match["result"]
match
match.groups
match.groups()
match.groups("result")
match.groups("resulta")
match.groups()
match.group("result")
match = re.match(".*Rs\=(?P<result>.*)\|",x)
match.group("result")
match = re.match(".*Rs\=(?P<result>.*?)\|",x)
match.group("result")
import find_response as fr
reload fr
reload fr
reload (fr)
fr.get_response_string(x)
for (x, row) in short.iterrows():
    print(fr.get_response_string(row['_raw']))
    
for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw']))
for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw'])
for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw'])



)

)
[for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw']))]
[for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw'])]


)
[for (x, row) in short.iterrows(): yield(fr.get_response_string(row['_raw'])]





)
data
data[:1]["_raw"]
data
data.apply(lambda row: row['result'] = fr.get_response_string(row['_raw']))
data.apply(lambda row: fr.get_response_string(row['_raw']))
data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1)
results = [data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1)]
results
results = [data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1)]
results
results = [data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1), reduce=false]
results = [data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1, reduce=False)]
results
results[1]
type(results)
results = data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1, reduce=False)
type(results)
results
results[1]
results[:10]
results[0]
results[2]
results = data.apply(lambda row: fr.get_response_string(row['_raw']), axis=1, reduce=False)
[for i, row in results.iteritems(): yield row]
[for i, row in results.iteritems() yield row]
[for i, row in results.iteritems() yield row]
for i, row in results.iteritems():
    row
    
for i, row in results.iteritems():
    print(row)
    
for i, row in results.iteritems():
    
    
    print row
    
errorList = []
for i, row in results.iteritems():
    if(len(row) > 0):
        errorList.append(row)
        
errorList
errorsDf = pd.DataFrame(errorList)
errorsDf
errorsDf.index
errorsDf.index.names
errorsDf.index.name
errorsDf.index.names
errorsDf = pd.DataFrame(errorList, names=hello)
errorsDf = pd.DataFrame.from_items(errorList, orient=index, columns=['result'])
errorsDf = pd.DataFrame(errorList, names=hello)
errorsDf = pd.DataFrame(errorList)
errorsDf
errorsDf['1']
errorsDf[1]
errorsDf[0]
errorsDf.groupby(0)
something = errorsDf.groupby(0)
something
something.sum()
errorsDf.groupby(0).agg(0)
errorsDf
errorsDf[:1]
errorsDf.groupby(0).agg()
errorsDf.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
errorsDf.groupby(o).apply(lambda x: 100*x/float(x.sum()))
errorsDf.groupby(0).apply(lambda x: 100*x/float(x.sum()))
something = errorsDf.groupby(0)
something.groupby(level=0).apply(lambda x: 100*x/float(x.sum()))
something.apply(lambda x: 100*x/float(x.sum()))
something.groupby(level=0)
errorsDf.groupby(0)
errorsDf.groupby(0)
_201
_i201
_201.plot()
errorsDf.rank()
errorsDf
errorsDf[0]
errorsDf.groupby(0)
groupBy = errorsDf.groupby(0)
import numpy as np
groupBy.aggregate(np.sum)
r = groupBy.aggregate(np.sum)
r
r.pivot_table()
r.pivot_table
r.pivot_table
r
groupBy
groupBy.rank()
groupBy.cumcount()
dir()
list
errorList
errorDf
errorsDf
errorsDf.cumsum()
errorsDf
errorsDf.apply(pd.Series.value_counts)
error_counts = errorsDf.apply(pd.Series.value_counts)
error_counts
type(error_counts)
error_counts[0]
error_counts.ndim
error_counts
error_counts.plot
error_counts.plot()
error_counts.plot()
get_ipython().magic(u'pylab')
error_counts.plot()
type(error_counts)
error_counts.plot(kind=hist)
error_counts.plot(kind='hist')
error_counts.plot(kind='bar')
error_counts[:10].plot(kind='bar')
error_counts[:10].plot(kind='barh')
error_counts
error_counts[:20].plot(kind='barh')
error_counts[1:20].plot(kind='barh')
error_counts[1:11].plot(kind='barh')


import pandas as pd
get_ipython().magic(u'pylab ')
x = pd.read_csv('StdDevValues.txt')
x
x['Values']
x['Values']
x['Values']
import numpy as np
np.std(x['Values'])
x.std('Values')
x.std()
get_ipython().magic(u'pinfo x.std')
x.plot(kind='line')
x.plot(kind='density')
x.std()
np.std(x['Values'])
x
np.var(x)
np.sqrt(np.var(x))
np.std(x)
np.mean
np.mean(x)
np.var(x)
get_ipython().magic(u'ls /Users/johnlo/Documents/')
get_ipython().magic(u'ls -all StdDev.xlsx')
y = pd.read_excel('StdDev.xlsx')
y
y = pd.read_excel('StdDev.xlsx')
y
y = pd.read_excel('StdDev.xlsx')
y
y
y['Numbers']
x1 = y['Numbers'][:17]
x1
np.var(x)
np.var(x1)
quit()
quit()

quit()

import pandas as pd
x = pd.DataFrame([7,9,9,10,10,10,10,11,11,13])
x
x.std()
x.std() * x.std()
x.mean()
x.std() * x.std()
x.std(ddof=1))
x.std(ddof=1)
x.std(ddof=0)
std = x.std(ddof=0) 
std * std
x.sum()
x
x.sum()
x.pow(2)
x.pow(2).sum()
y = pd.DataFrame([3,3,6,7,7,10,10,10,11,13,30])
y.pow(2)
y.pow(2).average()
y.pow(2).mean()
y.pow(2).sum()
r
R
get_ipython().system(u'R')
y.pow(2).sum()
y
y + 2000
(y + 2000).std()
y.std()
(y*1.10).std()
1.0 / 38.0

x = get_ipython().getoutput(u'pwd')
x
x.str()
str(x)
file(x + '/delme.css')
file(str(x) + '/delme.css')
file(str(x) + '/custom.css')
file(str(x[0]) + '/custom.css')
file(str(x[0]) + '/delme.css')
file(str(x[0]) + '/custom.css')
quit()

get_ipython().run_cell_magic(u"file('custom.css')", u'', u'')
get_ipython().run_cell_magic(u'bash', u'', u"%%file('custom.css')\n")
quit()
quit()

t = 2
t
get_ipython().magic(u'load find_dna.py')
def find_letters(s):
	t = 0
	a = 0
	g = 0
	c = 0
	for c in s:
		if c == 'C':
			c = c + 1
		elif c == 'T':
			t = t + 1
		elif c == 'A':
			a = a + 1
		elif c == 'G':
		    g = g + 1
	return str(a) + " " + str(c) + " " + str(g) + " " + str(t)

print(find_letters("GCTACACGGCCTTAA"))

def find_letters(s):
	t = 0
	a = 0
	g = 0
	c = 0
	for c in s:
		if c == 'C':
			c = c + 1
		elif c == 'T':
			t = t + 1
		elif c == 'A':
			a = a + 1
		elif c == 'G':
		    g = g + 1
	return str(a) + " " + str(c) + " " + str(g) + " " + str(t)

print(find_letters("GCTACACGGCCTTAA"))

get_ipython().magic(u'load find_dna.py')
def find_letters(s):
	t = 0
	a = 0
	g = 0
	c = 0
	for ch in s:
		if ch == 'C':
			c = c + 1
		elif ch == 'T':
			t = t + 1
		elif ch == 'A':
			a = a + 1
		elif ch == 'G':
		    g = g + 1
	return str(a) + " " + str(c) + " " + str(g) + " " + str(t)

print(find_letters("GCTACACGGCCTTAA"))

get_ipython().magic(u'load find_dna.py')
def find_letters(s):
	t = 0
	a = 0
	g = 0
	c = 0
	for ch in s:
		if ch == 'C':
			c = c + 1
		elif ch == 'T':
			t = t + 1
		elif ch == 'A':
			a = a + 1
		elif ch == 'G':
		    g = g + 1
	return str(a) + " " + str(c) + " " + str(g) + " " + str(t)

print(find_letters("GTTTCCTTGCGCACTAAGCACAGAGAAAGCATAAGCGAACGAAAGCAGACGCATCTCTGCTTCAGTGCGAGGATCTACGGTTGGTTCACCGCGCATCCTCGTTTTGAAACGTCATCGGGCTTCCCCCTAGCAGAAAAGGATCCTTAGGGTGAAATGACAAACTGCGACCTGCACCCTCCAGACCCAGATATCTCGGTACTAGCTCTTGCGGCACTCCAACCTGGATGGCTCAGTACGCTGTAGAGGGTGGGCTGGAAGCACGAGTTGCATAATAAGACTCTGAGCGGGCACGACTTTGAGCGAAACTTGGCCACTCCTAACGTAAGGATAATCTTTAGGCGGATTCCACTTGAAGCAAGTGCCAAGTAGTGACAGTGGTACGACGCTTTTTGGGTAATTCGAATGTCGGACGTGGTTCTTTACAATAGGAACCCTATTTATCTGGATGATGTCCCGAATTTGGGGCAGCCGCAAATTACGTGAGCCTTTCGGTTCACGGTGGATAGCCATAAAGCAGGCCCAGTATGCCGGCCGAGAACGAGAATCGTCCAGAGGTGAAGTGGTTTCCGCGCCTAGCGTCGTTTTAGGCGTATTGGCCGACAACTTAGCAGTAAAACGTTGGAGTACTAAGTGCGTTAACATTATACGTATTCGTGGCCTTATGTTGTGATCAGGCATGGAACCGTTCTCATGCTATAAAGGGGGAGTGATTAGATCGCAACCAAACGCGCTAGCGAGGTCGTCGGGATGCCAGATGGATCATTCTGCATAGTACCAGGCGTAGAAGGGCAGTTTGACTCTTCGTACTCCGAGACAGCGACTAGTCATTGTGTGGAACATGAGTAAATAGTTATAAAGGAAAACTTTGGAGTCAGCGATACGTACACGATGAACCATTCCATTATCCATAGGACTGGAAGA"))

st dna_to_rna.py
st dna_to_rna.py
exit()

"AAAATTT".replace("T", "U")
get_ipython().magic(u'load dna_to_rna.py')
def dna_to_rna(s):
	return s.replace("T", "U")

dna_to_rna("CGCTTTAGCCCCGTGAGTAGGCAGAAAACTGAAGGACCCGGTTATTCGTAATAATGCATGCCCTTGCCGTGTCTAGTTTAGTGGACTTAAACACGCTGGTACCCTCTATTAATGCTCTAGCCTGGTGGTTGTCTCCAACGTACAATATAGAGGTGTCATAAAACTTGTGACTGACCTCACTGACTCGACAGTGGGGTCCATGCAGACCGCTTGGCCCCGGCCGCAAGAATAGGGACGTTACATATAGCAGGACTGAACTCAGTCCTGACTACGACTTGCAAGAAGAGGGATCGTTCTACCCGGTGGAACAACGACGAAAATGACGAACGTCACAAATCCAAGGAGTCATCTAAATACAGGCTTATCCTGGTCCGTAACGAACTTTCCCGATCTCAGCCCGAAAGGGGTGTTCGCCAGTAGTCGTGGCACGACGTCAGTACTTGCTGACCCGTTGCAGGTCGATAAAAGGACAGGTTAAGTGCAAGCTTTGGATAGTGTAGTACATCTGACATGCGGATGTTGTTGGGCAGTATACAAGCGCTATCCTCCCCCCGGGCGTACGAACGCGCATTCTGCACCCGCCTCGCCTAGACTCAGGTAGTGTCTAAGGTTTGGTGTGTCGTTCTGGGACTTAGGACACTCTACAGGGCACCTGGGCCCACCTCAGGCCTCTCCTTGGGAATGCAGACTTCGAATCCGCGGCAAATGCTTCTGAACGGGTATTACTTAGACCGCATACCAATTGAACCGTCAAGGATAGTTTATGAACACTGAAGGCTTTCCTATATCGATAGCACGTGAGTACGCAAACCCACCGCGCGAAGGTAAATCTGTCACTCAGTTTCAGCTTAAGCGGAGCATGCCGCACCGGCGCTAAGTTCTGTCTAAATCTCCGTTGATT")

get_ipython().magic(u'pwd ')
get_ipython().magic(u'load dna_to_rna.py')
def dna_to_rna(s):
	return s.replace("T", "U")


dna_to_rna("TGGATGTACGGAAAAGGGAACCGCACCCGATCTAGTAGATCGATAAGTCGGCACATCGTGCAGTAGGCGCTCGATCTTATTCAATGTGGAATCTCTTGATGACTATGTAGCATTTAGAGCTGCATACCACACGAGCGTCTTTGTTCAGAGGGTCGACGGTGCGTGATTGGATCTGCGCGCTCGCACGGGCGACCCATGTCCGAGCATGGGATTCCGGAGAGTGTAAGACCACCTTTTAAGCAGGGGAAAATGAGTCCGGTTCCAGCCAAAACGGAGTCCCTGAACTGCTCCTCTGCAGTACTAAAAACTCACGTGATTAAGCTGTCCTGTCAATCCATTGTTAATCTAGGGGTTGTGTCGGTCCAAGACGTGCCATACAGGCCTGCGCGCACTTAGTGACAATGACGGTCTATTCAAGCGTGGCAGTCAGAAGAAAGCTGGTCTAATCCATTTTATCTCGCATGCAACAAATAAGTTAGTCCTATCCGCGTTTCACCTAACCAAGAGTGGAAATCTGTGACATGGGCTCCGAAGCATGGAAGTGCTGGAGATGCGACCGCTCTTTAGCGAATATTAGTCAATTGTGAGAAACCTTGTATACAGCACTAGTGTATTCATGCAGCGACACTTCGTTCTGACGCTTGCAATAACTGACCCTTCTAGTGAAGCTTTAGGTTAAAGAAAAGACCGCACCCTCAGATTCTATCCTGGATACTTTACGATTCGAGTAAGACACATAGCGCAGGTAAGTGGGTCAGGCAACATTATAACGGTCCGGTACAGTACGATAATACGCTACGCTTGAAATCATGATGTTTCCTCCCCGGTGTGTAGACGCCAGCTAGACACCGCGGATCTCCGAAGTATAATGGAAACAGTTTGAATTATCCTTTGGTGGAACATCGCACGGCACAGAAGTCCAAACGGCTAAACCATACTACTTACCCCCCATTTCACCTATTCACGTCGCAACCTCCGTCGTCAAAAGGCGCATCTCG")

quit()

import pandas as pd
from pandas import DataFrame, Series
DataFrame.inull(1)
DataFrame.isnull(1)
DataFrame([1,2,4])
x = DataFrame([1,2,4])
x
mean(x)
x.mean()

rand(10)
random(10)
import pandas as pd
import numpy as np
np.random(10)
np.random()
random.rand(10)
np.random.rand(10)
np.random.rand(10)
np.sort(np.random.rand(10))
get_ipython().magic(u'time (np.sort(np.random.rand(10)))')
get_ipython().magic(u'time (np.sort(np.random.rand(100000)))')
get_ipython().magic(u'time (np.sort(np.random.rand(100000)))')


quit()

quit()

get_ipython().system('cat ../ipython/log_all.py')
get_ipython().system('cat ../ipython/log_all.py')
exit()

get_ipython().system('cat ../ipython/log_all.py')
exit()

import script1

from imp import reload
reload(script1)
reload(script1.py)
from imp import reload
import script1
reload(script1)
reload(script1)
import platform from sys
from sys import platform
platform
from string import ascii_lowercase
ascii_lowercase
ascii
ascii()
ascii('aaa')
get_ipython().magic('load_ext')
get_ipython().magic('load_ext autoreload')
import script1
get_ipython().magic('edit script1.py')
import script1
import script1
reload script1
reload(script1)
reload(script1)
exit()

from do_shrubbery import do_shrubbery
from do_shrubbery import do_shrubbery;
from do_shrubbery import shrub
from do_shrubbery import shrub
from do_shrubbery import shrub
shrub()
spam()
from do_shrubbery import shrub
shrub
get_ipython().show_usage()
get_ipython().system('ls -F --color ')
dir()
from do_shrubbery import spam
spam()
from imp import reload
reload(do_shrubbery)
import do_shrubbery
do_shrubbery.title
reload(do_shrubbery)
do_shrubbery.title
do_shrubbery.title
from do_shrubbery import title as z
z
a = (1,2)
append(a, 9)
list(a)
list(a).append(3)
a
tuple(list(a).append(3))
x = list(a).append(3)
x
x = list(a)
x.append(3)
x
tuple(x)
exit()

2 ** 500
1 / 0
throw('foo')
raise('foo')
raise(new Exception('foo'))
raise( Exception('foo'))
raise(Exception('foo'))
e = Exception('Shubbery!')
e
raise(e)
import script1
import do_shrubbery
do_shrubbery.raise_exception()
l = [1,2]
get_ipython().system('ls -F --color ')
l
l.append(l)
l
type(2)
2.add(2)
2.bit_length
2.bit_length()
type(2)
x = 2
x.bit_length()
x =1
x.bit_length()
x = 5
x.bit_length()
x = 2 ** 500
x
x.bit_length()
x = 2 ** 99
x.bit_length()
l
l[2]
l[2][2]
l[2][2][2]
l
l = 1
x = (1,2)
list(x)
y = list(x)
y.append(3)
y
tuple(y)
r = {'food':'spam','taste':'yum'}
type(r)
r.food
r['food']
r['taste']
list(r)
list(r.values)
list(r.values())
list(r.keys())
letters
from string import ascii_lowercase as letters
set(letters)
s = set(letters)
s
'y' in letters
'y' contains letters
x = 1
type(x)
x = 2.2
type(x)
3.1415 * 2
import math
math.pi
import random
random.choice(range(1,100))
random.choice(range(1,100))
random.choice(range(1,100))
s = 'Spam'
len(s)
s[1:3]
s[1:]
s[0:3]
s[:3]
s + ' and shrubbery are the foundation'
s
s[0] = 'a
s[0] = 'a'
s[0] = 'z'
s = 'z' + s[1:]
s
s = 'spam'
shrub = 'shrubbery'
shrub
l = list(shrub)
l
l[1] = 'c'
''.join(l)
scrub = ''.join(l)
scrub
zip(l)
l
x = zip(l, l)
l
x
x = list(zip(l, l))
x
line = 'aaa,bbb,cccccc,d'
line.split(',')
type(line)
dir(line)
help upper
:help
s
s + 'NI!'
s.__add__('NI!')
help(s.replace)
help(s.find)

'{:>30}'.format('right')
'{:>20}'.format('right')



d = {"foo":"bar"}
d
d.key()
d.keys()
list(d.keys())

















list(d.keys())
















'%s' % 'foo'
'%s' % 'foo'







import packagetest/somefunc
import packagetest.somefunc
import packagetest.somefunc
somefunc.message()
import packagetest.somefunc.message as message
import packagetest.somefunc.message as message
from  packagetest.somefunc.message import message as message
from  packagetest.somefunc import message as message
messag()
message()
import packagetest.somefunc
somefunc.message()
packagetest.somefunc.message()
from packagetest import somefunc
somefunc.message
somefunc.message()
{"foo":"bar"}
x = {"foo":"bar"}
x
type(x)
x['boo'] = 'rebar'
x
list(x)
tuple(x)
x
x.items()
type(x.items())
list(x.items())
y = list(x.items)
y = list(x.items())
y
y[0]
type(y[0])
type(y[0][0])
y[0]
y[0][1]
y[0][0], y[0][1]
y[0][0], y[0][1] == y[0]
(y[0][0], y[0][1]) == y[0]
(y[0][0], y[0][1])
y[0]
(y[0][0], y[0][1]) == y[0]
while True:
    pass

class MyEmptyClass:
    pass

a = MyEmptyClass()
type(a)
def fib(n):
    a,b = 0,1
    print(a)
    a, b = b, a+b
    
fib(10)
def fib(n):
    a,b = 0,1
    print(a, b - b, a + b)
    
fib(10)
fib(20)
def fib(n):
    while (a < n):
        print(a, a, b=b, a+b)
        
it

import fib
import fib

import fib
fib(20)
fib.fib(20)
fib.fib(2000)
fib.fib(20000)
fib.fib(5000)
fib.fib(10000)
exit()

import fib
get_ipython().magic('pinfo fib.fib')
help(fib.fib)
help(fib.fib)
from imp import reload
reload(fib)
fib(10)
fib.fib(10
)
reload(fib)
exit()









































import fib
fib(2000)
fib.fib(2000)
fib.fib(2000)[-1]
import math

import math
import fib
fib.fib(2000)[-1]
fib.fib(2000)
fib.fib(200000)[1]
fib.fib(200000)[-1]
fib.fib(200000)[-5:-1]
fib.fib(2000000)[-5:-1]
51429 + 31781
514229 + 317811
exit()



