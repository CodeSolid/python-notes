
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

