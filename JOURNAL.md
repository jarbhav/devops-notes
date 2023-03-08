# Project Objectives
* Able to work with different datasets
* Recognizes which word belongs to which category
* Context sensitive spell checking

# 2023-02-14

## Problem statement
Swipe Typing algo for better matching link.
Unlike the keyboard-based swipe typing approach, the Categorizer framework does not support spell correction. It also cannot perform pattern matching when the order of the attributes (for ex, ifsc, party name, etc.) changes.
### Proposed Solution
A module that can perform spell correction and also map attributes to a category, irrespective of the order in which they occur.

## Meeting notes
1. Portfolio mgmt app has different sources of data which contains spelling errors. Example: OCR
2. Provided dataset of words if certain letters are coming predict the word correctly
3. Make POC 
4. Maintain journal - log tasks / problem / challenges / solution / logical point
    * daily(during research) / alternatively (during coding)
5. Guidelines
    * Do the work in phases
    * req analysis
    * design phase
    * Code
    * testing / validation

6. API requirements
    * Swagger UI
    * Configurable (able to work with different datasets)


# 2023-02-15

## Research on spelling correction algorithms

### Approaches
1. Algorithmic
    * **SymSpell Algorithm** 
    > Time complexity is `O(1)`
    >
    > [Github](https://github.com/wolfgarbe/SymSpell)
    >
    > [Blog](https://seekstorm.com/blog/1000x-spelling-correction/) 

    * **LinSpell**
    > Time complexity is `O(N)`
    >
    > A linear scan through the word list and calculating the edit distance for every single word
    >
    > [Github](https://github.com/wolfgarbe/LinSpell/)

    * **BK - Tree** 
    > Time complexity is `O(log dictionary_size)`
    > 
    > [Blog](https://nullwords.wordpress.com/2013/03/13/the-bk-tree-a-data-structure-for-spell-checking/)

    * **Norvig Spell Checker** 
    > Time complexity is `O(e^(max edit distance))`
    >
    > [Blog](http://norvig.com/spell-correct.html)

2. ML
    * [Neural Network based approach](https://analyticsindiamag.com/neuspell-a-neural-net-based-spelling-correction-toolkit/)
    * [Python package](https://github.com/neuspell/neuspell)


## Findings
There are two specific forms of spelling correction:
1. Isolated-term correction
    * edit distance
    * k-gram overlap
2. Context-sensitive correction
    * [Theory](https://nlp.stanford.edu/IR-book/html/htmledition/context-sensitive-spelling-correction-1.html)
    * [String Metric](https://en.wikipedia.org/wiki/String_metric)
    > There are many different string metrics like: 
    >
    > [Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance)
    >
    > [Damerau-Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
    >
    > [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
    >
    > [Jaro-Winkler](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)
    > 
    > [Strike a match](http://www.catalysoft.com/articles/StrikeAMatch.html 
)

3. Weighted Edit distance gives a higher priority to pairs which are close to each other on the keyboard layout or which sound similar

4. Use SymSpell, if speed is important. It is 2–3 orders of magnitude faster than BK-Tree and 5–6 orders of magnitude faster than Norvig’s algorithm.
5. Use LinSpell, if memory usage is important. It is 10* faster than BK-Tree for same memory usage


# 2023-02-16

## Algorithm
Linear Search Spelling Correction (LinSpell Algorithm)

## Data input
Frequency dictionary

## Working
* Damerau - Levenshtein Distance between the input word and words in the frequency dictionary is calculated
* This takes linear time
* Words with the shortest distance and highest frequency are suggested

## Implementation
* Writing the implementation in python
* Will compare the performance with a better algorithm

# 2023-02-17

## Restricted Damerau - Levenshtein Distance (optimal string alignment)
The number of insertion, deletion, substitution, and transposition edits required to transform one string to the other. This value will be >= 0, where 0 indicates identical strings.

This algorithm is basically the Levenshtein algorithm with a modification that considers transposition of two adjacent characters as a single edit.
This is the simpler and faster optimal string alignment (aka restricted edit) distance that differs slightly from the classic Damerau-Levenshtein algorithm by imposing the restriction that no substring is edited more than once. So for example, "CA" to "ABC" has an edit distance of 2 by a complete application of Damerau-Levenshtein, but a distance of 3 by this method that uses the optimal string alignment algorithm.

Optimal string alignment algorithm computes the number of edit operations needed to make the strings equal under the condition that no substring is edited more than once
Damerau–Levenshtein distance - Wikipedia 

## Tasks Done
* Implemented Linear Search Spelling Correction Algorithm
* Implemented Symmetric Delete Spelling Correction Algorithm
* Two endpoints created for each of the algorithms respectively
* Basic Testing of both endpoints completed
* Organized the Code

# 2023-02-20

## API endpoint details

* Made using a framework called FastAPI + Python
* Each endpoint has has three parameters:
    1. Input String (Path parameter) : The string to be checked
    2. Verbosity (Query Parameter) : Verbosity of spelling suggestions
        * Top match - 0
        * Closest match - 1
        * All matches - 2
    3. Edit Distance (Query parameter) : The max distance within which a search for correct spelling will take place (default 2)

### Root Endpoint
![Root Endpoint](/images/api/1.png)

### First Endpoint
![First Endpoint](/images/api/2.png)

### Second Endpoint
![Second Endpoint](/images/api/3.png)


## Suggestions from the meeting
1. Make the *verbosity* as enum instead of integer
2. Mention errors clearly in the response
3. Write function for dataset creation
4. Measure the performance difference between the two endpoints
5. Implement Error correction on multiple words

## Client Data details

1. For spelling correction, only the ‘transaction details’ column of the dataset is useful as it is the only column with english words
2. In each row there are entries separated either by ‘/’ or by ‘ ‘.
3. Regarding frequency dictionary creation from client data:
    * Entries in each row will be first separated wrt the two delimiters mentioned above
    * Numerical values obtained after the first step will be ignored

## Thoughts
After constructing the frequency dictionary with the client data, if the working of the algorithm is not satisfactory, then search for a better approach

## Tasks done
* Changed the type of verbosity parameter to enum
* Implemented Error Handling
* Identification of useful fields in the client data
* Started writing code for frequency dictionary generation

# 2023-02-21

## Frequency dictionary generation from client data
* Extracted words using pandas and regex
* Original Client data had 1693845 rows and 6 columns
* ‘xn_details’ column containing transaction details only had english words
* From ‘xn_details’ column 140345 words were obtained

### Observations:
* Some words have wrong spelling
* Some words are incomplete
* Some words are abbreviations

## New features of the algorithm

* Words extracted from client data to be put into categories for context sensitive spelling correction
* Few Categories:
    1. person name
    2. Designation
    3. Banking related terms
    4. actual english words
    5. location
    6. bank name
    7. company name
* Ignore single letters
* Abbreviations to full form and vice versa
* Algorithmic approach for categorization preferred

## Potential Approach
* First categorize transactions based on type (UPI / NEFT / IMPS etc.)
* After categorization make separate parsing rule for each type of transaction
* Using such parsing rules extract words/terms from each transaction and keep categorizing them into above mentioned categories at the same time count their frequency

# 2023-02-22

## Data Cleaning
1. Remove single letter entries 
2. In every transaction entry remove from the start any number, whitespace, ‘:’, ‘\t’
3. Split on ‘\t’ check for length 1 list if only alphabets then keep else drop
4. Singled out the transaction details column, cleaned and sorted and standardized it

## Extracting Individual words
* First put all the transaction entries into two broad categories:
    * Transactions having ‘/’ - G1
    * Transactions not having ‘/’  - G2
* In G1 (1598735)
    * Divide based on whether entries start with ‘/’
        * Starting with ‘/’ (879)
            * Split based on ‘/’ then for each token:
            * If only numbers : Drop
            * If alphanumeric : drop
            * If only alphabets and symbols like ‘_’ : keep
            * If multiple words separated by ‘ ‘ : Perform NER

### TODO
Find a way to categorize words found using the method above:
* RegEx
* Dictionary / wordlist

>Named-entity recognition (NER) (also known as (named) entity identification, entity chunking, and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.


# 2023-02-23

## Tasks Done

* For transaction entries starting with ‘/’ symbol, different words have been separated out
* Next task is to divide them into categories
* Entries which have both ‘:’ and ‘/’ split based which symbol occurs more times
* For transaction entries who have a ‘/’ symbol in between, different categories of transaction have been identified as:
    * `ATM-CASH/+ <ADDRESS>/<LOCATION>/<NUMBER>`
    * `ATM-CASH/++<ADDRESS>/<LOCATION>/<NUMBER>`
    * `RD/<NUMBER>/<NAME>`
    * `BRN-<NUMBER>:<INFO>/<TYPE>`
    * `BRN-<NUMBER>/<TYPE>`
    * `BRN-BKNG-REF NO.<ALPHANUMERIC> USD <NUMBER>`
    * `BRN-REF NO <ALPHANUMERIC> USD <NUMBER>`
    * `BRN-BY CASH <?>/<?>`
    * `BRN-CLG-CHQ PAID TO <NAME> /<BANK>`
    * `BRN-RTGS-<ALPHANUMERIC>-<NAME>-Y/S`
* Remove numbers, comma, fullstop from the right and left side of words
* Remove dates

# 2023-02-24

* Attended the Google Cloud Day, security track

## Meeting Notes
1. Count frequency of special characters per entry and in the whole document write a logic for separator based on that
2. Look for a method other than NLP for categorization


# 2023-02-27

## Work

* Reading the data using read_csv method, while using ‘\t’ as separator
* 40 lines were dropped since they had more than 6 columns
* Dataframe size after reading is (1693805, 6)
* Counted the occurrence of special characters in the whole data
    * '/': 22168690
    * ' ': 9950625
    * '-': 986039
    * ':': 151603
    * '.': 132082
    * '_': 109966
    * '@': 45130,
    * '%': 45110,
    * '+': 20970,
    * '(': 19107,
    * ')': 11207,
    * '#': 10412,
    * ',': 6566,
    * '*': 4580,
    * '[': 3383,
    * '&': 3000,
    * ']': 2085,

* Most common separator is ‘/’ but not every transaction entry has ‘/’
So to decide the separator, choose the the most common special character per transaction
* If a transaction has ‘ ’ as the most common special character, don't split it, instead put such transaction separately and process them separately creating rules for each type of transaction
* If for a transaction, we have two or more separator as most common, choose the one which occurs most in the document overall
* After getting the appropriate separator for the transaction, split on that to get the words
* Pass the words obtained through a filter which removes strings which are:
    * Alphanumeric
    * Numbers
    * Dates
    * Timestamps
    * Empty

## Problems
Coming up with an appropriate filter, to remove unwanted words


# 2023-02-28

## Meeting Notes

1. In the journal update details about the API implementation
2. For the already separated words
    * Sort them in descending order of frequency
    * Higher frequency words can directly be used
    * For the words with lower frequency come up with a logic to recognize useful words
3. Keep record of the separator in the previous line (high prob that it is the separator throughout the data, since only a single source of data comes at a time)
4. Regarding spelling errors already in the data decide on:
    * Excluding them
    * Correcting them and including in the data
5. Some transaction entries will have multiple separators
6. For entries with no separator, use NLTK to determine which are english words


## Thoughts
For the words with incorrect spellings in the dataset, maybe the previously built endpoint can be used

## Tasks Done / Observations

* Sorted already separated words in descending order:
    * Found a few irregularities, few of the words have not separated properly
* Need to modify the separation logic
* Lot of words were just dates and date ranges, those were dropped
* Some of the words extracted still had / , this is because of the separation logic
* Some words had special characters in the starting and ending:
    * ??
    * ?
    * <
    * (
    * /
    * \* 
    * &
    * '
    * )
* Did more data exploration

# 2023-03-01

* Working on improving the separation logic
* After data exploration, it is safe to say that [‘/’, ‘:’, ‘ ‘] are valid separators for a group of transaction
* Current algorithm idea:
    * Consider the frequency of ‘/’ and ‘ ‘ in overall document as their respective weights
    * In the second iteration, if separators found are:
        * ‘ ‘ -> store separately, don’t split
        * ‘ ‘  and ‘/’ -> 
            * `If count(/) * weight(/) > count(‘ ‘)  * weight(‘ ’), split on /. Else store separately`
        * ‘:’ and ‘ ‘ -> same as above
        * ‘/’ -> Split
        * ‘:’ -> Split
        * ‘:’ and ‘/’ -> split
        * All three -> if ‘:’ or ‘/’ wins then split on both, else store separately

## Observations
* [‘_ ‘,  ‘-’, ‘.’] can be valid separators for transactions where [‘/’, ‘:’, ‘ ‘] are not present

## Tasks done
Now the algorithm considers the case where there can be multiple separators. Working is explained above. Some improvements are still required

# 2023-03-02

* Working on finding the separators for the group of transactions where [‘/’, ‘:’, ‘ ‘] are not present.
* In this group special character frequency is as follows:
    * '-': 8284,
    * '_': 3125,
    * '.': 324
* Transactions can’t simply be split on these characters above as many banking terms have these characters in between

# 2023-03-03

Submitted the work done with documentation till now before switching into the DevOps team


# 2023-03-06

## Terraform

* Terraform is a tool for building, changing, and versioning infrastructure safely and efficiently
* The key features of Terraform are:
    * **Infrastructure as Code**: Infrastructure is described using a high-level configuration syntax. This allows a blueprint of your datacenter to be versioned and treated as you would any other code. Additionally, infrastructure can be shared and re-used.
    * **Execution Plans**: Terraform has a "planning" step where it generates an execution plan. The execution plan shows what Terraform will do when you call apply. This lets you avoid any surprises when Terraform manipulates infrastructure.
    * **Resource Graph**: Terraform builds a graph of all your resources, and parallelizes the creation and modification of any non-dependent resources. Because of this, Terraform builds infrastructure as efficiently as possible, and operators get insight into dependencies in their infrastructure.
    * **Change Automation**: Complex changesets can be applied to your infrastructure with minimal human interaction. With the previously mentioned execution plan and resource graph, you know exactly what Terraform will change and in what order, avoiding many possible human errors.
* [Key concepts](https://www.terraform-best-practices.com/key-concepts)
* [Terraform-GCP](https://cloud.google.com/docs/terraform) 

## Jenkins
* Jenkins is an open-source automation tool for Continuous Integration (CI) and Continuous Deployment (CD). The tool makes it painless for developers to integrate changes to the project.
* Jenkins' primary focus is to keep track of the version control system and initiate and monitor a build system if there are any changes
* Broadly divided into two components:
    * Master node
    * Worker nodes


## Ansible
* Ansible is an automation platform that makes your applications and systems easier to deploy and maintain. 
* Features
    * CI/CD
    * IaC
* [Architecture & Use Cases](https://k21academy.com/ansible/ansible-for-beginners/)
* [Basic Concepts](https://docs.ansible.com/ansible/latest/network/getting_started/basic_concepts.html)


## Kubernetes
* Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management.

### Terms
* When you deploy Kubernetes, you get a **cluster**.
* A Kubernetes cluster consists of a set of worker machines, called **nodes**, that run containerized applications. Every cluster has at least one worker node.
* The worker node(s) host the **Pods** that are the components of the application workload. 
* The ***control plane*** manages the worker nodes and the Pods in the cluster. 
* In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault-tolerance and high availability.

![Architecture](/images/api/components-of-kubernetes.svg)
* [Kubernetes Components](https://kubernetes.io/docs/concepts/overview/components/)


## Docker

* Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. 

* [Docker: Components (Client, Host, Daemon, etc.)](https://blog.knoldus.com/docker-components/)
* [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
* [Compose file specification](https://docs.docker.com/compose/compose-file/)


## Gitlab
* Gitlab is a complete DevOps platform that enables professionals to perform all the tasks in a project—from project planning and source code management to monitoring and security
* [GitLab architecture overview](https://docs.gitlab.com/ee/development/architecture.html) 


## Grafana
> Grafana is an open source interactive data-visualization platform, developed by Grafana Labs, which allows users to see their data via charts and graphs that are unified into one dashboard

## OpenShift
>OpenShift is a cloud development Platform as a Service (PaaS) developed by Red Hat. It is an open source development platform, which enables the developers to develop and deploy their applications on cloud infrastructure.

## OpenStack
> OpenStack is an Infrastructure as a Service (IaaS) platform, OpenStack enables companies to easily and efficiently add servers, storage and networking components to their cloud.

## Puppet
> Puppet is a software configuration management tool which includes its own declarative language to describe system configuration

## Vagrant
> Vagrant is an open-source software product for building and maintaining portable virtual software development environments

## Apache Tomcat
> Apache Tomcat provides a "pure Java" HTTP web server environment in which Java code can also run. 
Tomcat is a web server (can handle HTTP requests/responses) and web container (implements Java Servlet API, also called servletcontainer) in one.

## Other Concepts
> Infrastructure as a service (IaaS) is a cloud computing infrastructure that provides compute, network, and storage resources over the internet

> Platform as a service (PaaS) is a cloud infrastructure layer that provides resources to build user-level tools and applications. It includes the underlying infrastructure including compute, network, and storage resources, as well as development tools, database management systems, and middleware.

![Cloud Computing Models](/images/api/cloud-models.png)

[What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)

[Webhook](https://www.redhat.com/en/topics/automation/what-is-a-webhook) 

## Tasks Done
1. Learnt about various tools and concepts related to DevOps and documented them
2. Introduction to the DevOps team 

# 2023-03-07

* Setup GitLab account
* Wrote documentation about linux commands
* Converted Programmers's diary to markdown

# 2023-03-08

* Wrote documentation regrading git commands