#!/usr/bin/env python
# coding: utf-8

# # 💬 SMS Emergencial (Twilio API) 

# In[33]:


import os


# In[34]:


from twilio.rest import Client


# In[35]:


#SID da conta e token de autenticação da API

account_sid = "AC1335462d196114ea7df5e2529ab2be07"
auth_token = "50c4e8304b2dbe66caf5c1fe83486485"
client = Client(account_sid, auth_token)


# In[42]:


message = 'EVACUAÇÃO URGENTE!- Risco de deslizamento em sua área. Por favor, deixe sua casa imediatamente. Siga as instruções das autoridades locais e não tente retornar até que tudo esteja liberado. Fique seguro!'


# In[44]:


message = client.messages.create(
    body=message,
    from_='+12056516179',
    to=['+5511999771172', '+5511973530612', '+5511983563606', '+5511982163303']
)
print(message.sid)


# In[ ]:




