
.. image:: https://travis-ci.org/wmshort/multiwordnet.svg?branch=master
    :target: https://travis-ci.org/wmshort/multiwordnet

============
MultiWordNet
============

Background
----------
A WordNet is a lexico-conceptual database for a language. In a WordNet, a language's lexemes (nouns, verbs, adjectives, and adverbs) are grouped into sets of semantically related words called synsets (for "synonym sets"), which thus correspond to the senses that are lexicalized in the language. A WordNet also typically includes information about semantic relations (i.e., relations between synsets) and about lexical relations (i.e., relations between words).

Created by Stefano Minozzi between 2004 and 2008 as part of the Fondazione Bruno Kessler's MultiWordNet, the original Latin WordNet contained 9,124 lemmas drawn from Riganti's Lessico Fondamentale Latino. The University of Exeter's TExtual Project aims to build on and expand Minozzi's work by adding some 30,000 words, covering the Latin language from the archaic period to late antiquity (and somewhat beyond).

Installation
------------
To get setup, all you need to do is compile the relevant SQLite databases:

``from multiwordnet.db import compile``
``compile('latin')``

You will need to do the same for the English and Italian synset databases:

``compile('english', 'synset')``
``compile('italian', 'synset')``

To make full use of the semantic data that is included in the MultiWordNet, you will also want to compile the list of common relations and semfield hierarchy:

``compile('common')``

Basic usage
-----------

``from multiwordnet.wordnet import WordNet``

``LWN = WordNet('latin')``
``for lemma in LWN.lemmas:  # all the lemmas currently in the WordNet``
``   print(lemma.lemma, lemma.pos)``
``abalieno = LWN.get_lemma('abalieno', 'v')  # this gives you access to a single lemma``
``abalieno.synonyms  # all lemmas that share a synset with 'abalieno'``
``abalieno.antonyms``
``abalieno.derivates  # use .get_derivates('n') to restrict by POS``
``abalieno.relatives  # use .get_relatives('n') to restrict by POS``
``abalieno.synsets``
``LWN.get('abalien', strict=False)  # returns a list of lemmas using wildcard matching``
``LWN.get('abalien', pos='v', strict=False)  # restrict the results to verbs``
``synset = LWN.get_synset('n#07462736')  # you can find a synset directly, if you know its offset ID``
``synset.lemmas``

``LWN.get_relations(source=synset)  # all semantic relations where 'synset' is the source``
``LWN.get_relations(source=synset, type='@')  # restrict to hyponymy relations``

Relations are of the following types:
Noun relations
--------------
Semantic:
!   antonym
@   hypernym
~   hyponym
#m    member-of
#s    substance-of
#p    part-of
%m    has-member
%s    has-substance
%p    has-part
=    attribute
|    nearest
+r    has-role
-r    is-role-of
Lexical:
!   antonym
@    hypernym
~    hyponym
+c    composed-of
-c    composes
\    derived-from
/    related-to

Verb relations
--------------

Semantic:
!    antonym
@    hypernym
~    hyponym
*    entailment
>    causes
^    also-see
$    verb-group
|    nearest

Lexical:
!   antonym
@    hypernym
~    hyponym
+c    composed-of
-c    composes
\    derived-from
/    related-to

Adjective relations
-------------------
Semantic:
!    antonym
&    similar-to
=    is-value-of
^    also-see
|    nearest

Lexical:
!   antonym
<    participle
+c    composed-of
-c    composes
\    derived-from
/    related-to

Adverb relations
----------------

Semantic:
!    antonym
|    nearest

Lexical:
!    antonym
+c    composed-of
-c    composes
\    derived-from
/    related-to

``LWN.get_semfield_by_code('110')  # 'Furniture'``

Semfields
---------
160    Acoustics
187    Administration
123    Agriculture
142    Anatomy
125    Animal_Husbandry
145    Animals
188    Anthropology
96    Applied_Science
35    Archaeology
91    Archery
107    Architecture
19    Art
192    Artisanship
49    Astrology
113    Astronautics
139    Astronomy
87    Athletics
161    Atomic_Physic
225    Aviation
66    Badminton
204    Banking
67    Baseball
68    Basketball
62    Betting
141    Biochemistry
140    Biology
194    Body_Care
202    Book_Keeping
94    Bowling
89    Boxing
109    Buildings
63    Card
149    Chemistry
61    Chess
20    Cinema
3    Color
195    Commerce
128    Computer_Science
69    Cricket
77    Cycling
21    Dance
118    Dentistry
215    Diplomacy
85    Diving
29    Drawing
150    Earth
196    Economy
167    Electricity
168    Electronics
114    Electrotechnology
111    Engineering
201    Enterprise
146    Entomology
134    Environment
190    Ethnology
206    Exchange
1    Factotum
207    Fashion
90    Fencing
203    Finance
92    Fishing
191    Folklore
105    Food
70    Football
54    Free_Time
110    Furniture
163    Gas
106    Gastronomy
144    Genetics
165    Geography
151    Geology
157    Geometry
71    Golf
37    Grammar
31    Graphic_Arts
193    Health
34    Heraldry
33    History
80    Hockey
127    Home
9    Humanities
93    Hunting
115    Hydraulics
208    Industry
199    Insurance
42    Jewellery
209    Law
36    Linguistics
38    Literature
156    Mathematics
116    Mechanics
117    Medicine
152    Meteorology
7    Metrology
210    Military
205    Money
81    Mountaineering
25    Music
51    Mythology
227    Nautical
2    Number
43    Numismatics
48    Occultism
153    Oceanography
164    Optics
24    Painting
154    Paleontology
47    Paranormal
211    Pedagogy
5    Person
119    Pharmacy
32    Philately
39    Philology
40    Philosophy
26    Photography
159    Physics
143    Physiology
147    Plants
41    Plastic_Arts
58    Play
214    Politics
220    Post
120    Psychiatry
46    Psychoanalysis
8    Psychological_Features
45    Psychology
216    Publishing
129    Pure_Science
6    Quality
95    Racing
64    Radio_TV
121    Radiology
228    Railway
50    Religion
52    Roman_Catholic
82    Rowing
72    Rugby
212    School
44    Sculpture
217    Sexuality
78    Skating
79    Skiing
73    Soccer
169    Social_Science
218    Sociology
65    Sport
158    Statistics
84    Sub
122    Surgery
83    Swimming
74    Table_Tennis
200    Tax
219    Telecommunication
221    Telegraphy
222    Telephony
75    Tennis
28    Theatre
53    Theology
4    Time_Period
166    Topography
223    Tourism
108    Town_Planning
224    Transport
213    University
226    Vehicles
126    Veterinary
76    Volleyball
88    Wrestling
