# ChatGPT Mentions & Traffic Referrals Analysis

Analyse your brand's authority and citation patterns across ChatGPT. 
This toolkit helps you track down backlinks and traffic referrals from one or more ChatGPT searches, depending on how you structure the input XLSX file.

## 🔗 Link to the App 

- [ChatGPT Mentions Visualizer (Streamlit)](https://chatgpt-mentions-visualizer.streamlit.app/)

## 🚀 Use Cases

- **Analyze brand authority** over ChatGPT
- **Track backlink** from deep ChatGPT conversations
- **Identify traffic channels** most referenced by ChatGPT for citations


## 📝 Data Preparation

1. **Run a search on ChatGPT with the Search Mode on**  
![ChatGPT Search Example](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/chatgpt_search_1.png?raw=true)


2. **Open the ChatGPT Path Chrome extension**
![ChatGPT Path](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/chatgpt_path_extension_2.png)

3. **Run the Export**
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/export_raw_3.jpg)

4. **Data Cleaning and Save as .xlsx**
   - **Remove the top rows (up to Source)**
   - **Remove `Index` and `Timestamp` headers**
   - **Replace any `Type` header with `Prompt`** (this should contain the exact prompt you used on ChatGPT).
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/export_finesse_4.jpg)


## 📊 How to use the app

1. **Upload the cleaned XLSX file:**
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_no_search_box_%25.jpg)

As the app reads in the file, leave the red-circled box in the image below empty. This will give you an overview of the referrals sourced from the prompt. More on how this is calculated below.

6. **Fill up the brand box to see how many mentions for your domain**
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_6.jpg)

7. **Scroll for some Summary Stats**
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_summary_stats_7.jpg)

8. **Browse the full table in Data Overview**
![ChatGPT export](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/strealit_app_data_over_8.jpg)


## ⚠️ Caveats /& Notes

- **Rule-based Classification of Traffic Referrals**  
  The system may not function as expected if a specific traffic source appears in the raw ChatGPT output that is not included in the classification logic within the code.

- **Live Data Updates**  
  You can update the heatmap and data summaries in real time by entering a different domain in the search bar in real time.

- **Issues with Stochastic Output and Analytics Attribution**  
   Just a heads-up to signal that some analytics platforms (e.g., GA4) may fail to report traffic referrals from ChatGPT or other LLMs - perhaps it's still early days to demand proper attribution ffs.   
 Other than that, beware that ChatGPT and other LLM-based systems may generate non-existent URLs due to anomalies in large-scale probabilistic outputs or dysfunctions in their RAG systems. Be sure to verify if the extracted links exist.

- **The Streamlit App is Free to Use Outside This Space**  
  It's all vibe-coded and no password-protected files or APIs have been used - can't see a reason why the toolkit should not be free for use.

## 🛠️ Rinse and Repeat on **Perplexity** and **Claude**

Yes, you can potentially replicate the process from above to inspect how your brand is getting mentioned and see what SEO meta tags fit the bill across other LLMs. 

Despite pairing up to ChatGPT in terms of the underlying mechanisms involving probability distributions and RAG, Perplexity and Claude structure their output responses in slightly different ways. 

Fortunately, it's shipped with JSON. 

All you need is another raw JSON file you can extract using the following **JavaScript bookmarklets**:

### Perplexity Grounded Query Extractor

```javascript
javascript:(async()=>{const s=(location.pathname.match(/\/search\/([^/?#]+)/)||[])[1];if(s){const t=Date.now();const q=`with_parent_info=1&with_schematized_response=1&from_first=1&version=2.18&source=default&limit=100&offset=0&supported_block_use_cases=answer_modes&supported_block_use_cases=media_items&supported_block_use_cases=knowledge_cards&supported_block_use_cases=inline_knowledge_cards&_t=${t}`;const r=await fetch(`/rest/thread/${s}?${q}`,{credentials:'include',cache:'no-cache'});if(r.ok){const d=await r.json(),u=URL.createObjectURL(new Blob([JSON.stringify(d,null,2)]));Object.assign(document.createElement('a'),{href:u,download:`perplexity-${s}.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2e3);}}})();
```


### Claude Grounded Query Extractor

```javascript
javascript:(async()=>{try{const c=location.pathname.match(/\/chat\/([^/]+)/)?.[1];if(!c){alert('Open%20a%20Claude%20chat%20first');return;}const t=Date.now();const o=(await(await fetch(`/api/organizations?_t=${t}`,{credentials:'include',cache:'no-cache'})).json())[0].uuid;const j=await(await fetch(`/api/organizations/${o}/chat_conversations/${c}?tree=true&rendering_mode=messages&render_all_tools=true&_t=${t}`,{credentials:'include',cache:'no-cache'})).json();const u=URL.createObjectURL(new Blob([JSON.stringify(j,null,2)],{type:'application/json'}));Object.assign(document.createElement('a'),{href:u,download:`claude-${c}-rich.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2000);}catch(e){alert('Could%20not%20fetch%20rich%20conversation%20JSON');console.error(e);}})();
```


## 🔗 Links to Perplexity and Claude Meta Data Extractors 

- [Perplexity Meta Data Extractor (Streamlit)](https://perplexity-meta-data-extractor.streamlit.app/)
- [Claude Meta Data Extractor (Streamlit)](https://claude-meta-tag-extractor.streamlit.app/)
