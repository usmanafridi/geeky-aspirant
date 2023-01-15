import spacy
#loading the english language small model of spacy
en = spacy.load('en_core_web_sm')
stopwords = en.Defaults.stop_words

text = """ Marie Curie was one of the most accomplished scientists in history. Together with her husband, Pierre, she discovered radium, an element widely used for treating cancer, and studied uranium and other radioactive substances. Pierre and Marie’s amicable collaboration later helped to unlock the secrets of the atom.

Marie was born in 1867 in Warsaw, Poland, where her father was a professor of physics. At an early age, she displayed a brilliant mind and a blithe personality. Her great exuberance for learning prompted her to continue with her studies after high school. She became disgruntled, however, when she learned that the university in Warsaw was closed to women. Determined to receive a higher education, she defiantly left Poland and in 1891 entered the Sorbonne, a French university, where she earned her master’s degree and doctorate in physics.

Marie was fortunate to have studied at the Sorbonne with some of the greatest scientists of her day, one of whom was Pierre Curie. Marie and Pierre were married in 1895 and spent many productive years working together in the physics laboratory. A short time after they discovered radium, Pierre was killed by a horse-drawn wagon in 1906. Marie was stunned by this horrible misfortune and endured heartbreaking anguish. Despondently she recalled their close relationship and the joy that they had shared in scientific research. The fact that she had two young daughters to raise by herself greatly increased her distress.

Curie’s feeling of desolation finally began to fade when she was asked to succeed her husband as a physics professor at the Sorbonne. She was the first woman to be given a professorship at the world-famous university. In 1911 she received the Nobel Prize in chemistry for isolating radium. Although Marie Curie eventually suffered a fatal illness from her long exposure to radium, she never became disillusioned about her work. Regardless of the consequences, she had dedicated herself to science and to revealing the mysteries of the physical world."""
lst=[]
for token in text.split():
    if token.lower() not in stopwords:    #checking whether the word is not 
        lst.append(token)                    #present in the stopword list.
        
#Join items in the list
print("Original text  : ",text)
print("Text after removing stopwords  :   ",' '.join(lst))

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