# "Who are you" CERN Webfest 2015 project

We are creating a tool to help you learn more about people around you, and connect with those with similar interests or background.

### Deliverables

We are developing:
* a back-end tool to analyse public profile of a person
  * _input_:
    * person's Twitter and LinkedIn ID 
    * (optionally: also Google Scholar, FB? or even person's for web search?)
    * (optionally: the category - professional, hobby, all?)
  * _output_: tags for that person (+ weights? likelihoods? categories?)
* a front-end (web) interface to the back-end tool

### Tasks/components

* *Data collection* – sources -> text
  * __Azqa, Maria, Marija, Paweł, Mufutau__
  * API (limitations) and library investigation 
  * What data and metadata is available?

* *Text processing* – text (and metadata) -> tags
  * __Sabrina, Konst., Marija, Azqa, Maria__
  * how? What library to use (nltk, gate)?
  * dealing with synonyms, categories

* *Information analysis* – tags (words, cats, weight, time?) -> tag cloud
  * __Sabrina, Sebastian, Paweł, Mufutau, Konst.__
  * Testing different thresholds, weights, timing, person vs. the contacts
  * Building tag cloud (profile) of a person

* *Front-end (web) interface*
  * __Harris__
  * taking user id (Twitter handle, LinkedIn profile) as input
  * visualisation of results

### Coding and testing nvironment
* Linux virtual machine, login using SSH (`ssh [your CERN login]@tedxapp` on Linux or Putty on Windows)
* Firewall open for specific port:
```
sudo firewall-cmd --zone=public --permanent --add-port=8443/tcp
sudo systemctl restart firewalld
```

### NLTK
* http://www.nltk.org/install.html
* http://www.nltk.org/data.html
* https://github.com/nltk/nltk/wiki/Installing-Third-Party-Software
  * http://nlp.stanford.edu/software/lex-parser.shtml
  * http://nlp.stanford.edu/software/CRF-NER.shtml
  * http://nlp.stanford.edu/software/tagger.shtml
  * all ZIPs downloaded to /opt/nltk and unzipped
  * /etc/environment contains ```
CLASSPATH=/opt/nltk/stanford-ner-2015-04-20
STANFORD_MODELS=/opt/nltk/stanford-ner-2015-04-20/classifiers```
  * try ```python src/test/nltk-test.py```


### Some useful links
* https://docs.google.com/document/d/1vJncqSeDNEUWGPD0mNYWFLoSl7xSUsobCwbG88O2IJc/edit?usp=sharing
* the team: webfest2015-who-are-you@cern.ch (https://e-groups.cern.ch/e-groups/Egroup.do?egroupName=webfest2015-who-are-you -> members)
* initial proposal: https://webfest.web.cern.ch/content/who-you-are-analysing-public-linkedin-and-twitter-profiles
