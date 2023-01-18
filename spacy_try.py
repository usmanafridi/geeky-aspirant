import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
stopwords = en.Defaults.stop_words

text = """ When I returned to the common the sun was setting. The crowd about the pit had increased, and stood out black against
the lemon yellow of the sky-a couple of hundred people, perhaps. There were raised voices, and some sort of struggle
appeared to be going on about the pit. Strange imaginings passed through my mind. As I drew nearer I heard Stent's
voice: "Keep back! Keep back!" A boy came running towards me. "It's movin'," he said to me as he passed; "it’s
screwin' and screwin' out. I don't like it. I'm goin' home, I am." I went on to the crowd. There were really, I should
think, two or three hundred people elbowing and jostling one another, the one or two ladies there being by no means the
least active. "He's fallen in the pit!" cried someone. "Keep back!" said several. The crowd swayed a little, and I elbowed
my way through. Everyone seemed greatly excited. I heard a peculiar humming sound from the pit. "I say!" said
Ogilvy. "Help keep these idiots back. We don't know what's in the confounded thing, you know!" I saw a young man, a
shop assistant in Woking I believe he was, standing on the cylinder and trying to scramble out of the hole again. The
crowd had pushed him in. The end of the cylinder was being screwed out from within. Nearly two feet of shining screw
projected. Somebody blundered against me, and I narrowly missed being pitched onto the top of the screw. I turned,
and as I did so the screw must have come out, for the lid of the cylinder fell upon the gravel with a ringing concussion. I
stuck my elbow into the person behind me, and turned my head towards the Thing again. For a moment that circular
cavity seemed perfectly black. I had the sunset in my eyes. I think everyone expected to see a man emerge-possibly
something a little unlike us terrestrial men, but in all essentials a man. I know I did. But, looking, I presently saw
something stirring within the shadow: greyish billowy movements, one above another, and then two luminous
disks-like eyes. Then something resembling a little grey snake, about the thickness of a walking stick, coiled up out of
the writhing middle, and wriggled in the air towards me-and then another. A sudden chill came over me. There was a
loud shriek from a woman behind. I half turned, keeping my eyes fixed upon the cylinder still, from which other
tentacles were now projecting, and began pushing my way back from the edge of the pit. I saw astonishment giving
place to horror on the faces of the people about me. I heard inarticulate exclamations on all sides. There was a general
movement backwards. I saw the shopman struggling still on the edge of the pit. I found myself alone, and saw the
people on the other side of the pit running off, Stent among them. I looked again at the cylinder and ungovernable terror
gripped me. I stood petrified and staring. A big greyish rounded bulk, the size, perhaps, of a bear, was rising slowly and
painfully out of the cylinder. As it bulged up and caught the light, it glistened like wet leather. Two large dark-coloured
eyes were regarding me steadfastly. The mass that framed them, the head of the thing, was rounded, and had, one might say, a face. There was a mouth under the eyes, the lipless brim of which quivered and panted, and dropped saliva. The
whole creature heaved and pulsated convulsively. A lank tentacular appendage gripped the edge of the cylinder, another
swayed in the air. Those who have never seen a living Martian can scarcely imagine the strange horror of its
appearance. The peculiar V-shaped mouth with its pointed upper lip, the absence of brow ridges, the absence of a chin
beneath the wedge like lower lip, the incessant quivering of this mouth, the Gorgon groups of tentacles, the tumultuous
breathing of the lungs in a strange atmosphere, the evident heaviness and painfulness of movement due to the greater
gravitational energy of the earthabove all, the extraordinary intensity of the immense eyes-were at once vital, intense,
inhuman, crippled and monstrous. There was something fungoid in the oily brown skin, something in the clumsy
deliberation of the tedious movements unspeakably nasty. Even at this first encounter, this first glimpse, I was
overcome with disgust and dread. """
lst=[]

for token in text.split():
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
        
#Join items in the list
print("Original text  : ",text)
print("Text after removing stopwords  :   ",' '.join(lst))

new_list= ' '.join(lst)
# print(new_list)
print(len(text))
print(len(new_list))
# 1. Marine
# 2. Intrigue
# 3. North-South
# 4. Topography
# 5. Peninsula
# 6. Latitude
# 7. Meridian


# ## After using Stopwords in 
# 1. 
# Marine
# 2. 
# Intrigue
# 3. 
# North-South
# 4. 
# Topography
# 5. 
# Peninsula
# 6. 
# Latitude
# 7. 
# Meridian


# # 2ns passage answers 
# # Original

# 8. Amicable 

# 9. Blithe 

# 10. Disgruntled 

# 11. Defiantly 

# 12. Despondently 

# 13. Desolation 

# 14. Disillusioned

#after stopwords:

# import os
# import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Answer the questions from the following passage :\nMarie Curie accomplished scientists history. husband, Pierre, discovered radium, element widely treating cancer, studied uranium radioactive substances. Pierre Marie’s amicable collaboration later helped unlock secrets atom. Marie born 1867 Warsaw, Poland, father professor physics. early age, displayed brilliant mind blithe personality. great exuberance learning prompted continue studies high school. disgruntled, however, learned university Warsaw closed women. Determined receive higher education, defiantly left Poland 1891 entered Sorbonne, French university, earned master’s degree doctorate physics. Marie fortunate studied Sorbonne greatest scientists day, Pierre Curie. Marie Pierre married 1895 spent productive years working physics laboratory. short time discovered radium, Pierre killed horse-drawn wagon 1906. Marie stunned horrible misfortune endured heartbreaking anguish. Despondently recalled close relationship joy shared scientific research. fact young daughters raise greatly increased distress. Curie’s feeling desolation finally began fade asked succeed husband physics professor Sorbonne. woman given professorship world-famous university. 1911 received Nobel Prize chemistry isolating radium. Marie Curie eventually suffered fatal illness long exposure radium, disillusioned work. Regardless consequences, dedicated science revealing mysteries physical world.\nQuestions:\n\nWhy was Marie disgruntled?\n\nMarie was disgruntled because she learned that the university in Warsaw was closed to women.",
#   temperature=0.7,
#   max_tokens=24,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )