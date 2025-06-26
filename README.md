# LLM Brand Authority \& Citation Analysis Toolkit

Analyze your brand's authority and citation patterns across leading Large Language Model (LLM) search engines. This toolkit helps you track backlinks, traffic sources, and reference behaviors from LLM-generated content.

## 🚀 Use Cases

- **Analyze brand authority** over LLM search engines
- **Track backlink proportions** from deep LLM conversations
- **Identify traffic channels** most referenced by LLMs for citations


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
![Streamlit](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_no_search_box_%25.jpg)

As the app reads in the file, leave the red-circled box in the image below empty. This will give you an overview of the referrals sourced from the prompt. More on how this is calculated below.

6. **Fill up the brand box to see how many mentions for your domain**
[!streamlit_](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_6.jpg)

7. **Scroll for some Summary Stats**
[!stats](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/streamlit_app_summary_stats_7.jpg)

8. **Browse the full table in Data Overview**
[!data overview](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/images/strealit_app_data_over_8.jpg)


## ⚠️ Caveats \& Notes

The app generates a heatmap, with the Y-axis showing link occurrences by traffic referral source.
- **Source Classification:**
Link sources are classified using rule-based logic and labeled accordingly.
- **Live Data Updates:**
Enter your domain in the search bar to update the heatmap and data summaries in real time.
- **Attribution Issues:**
Some analytics platforms (e.g., GA4) may not accurately report traffic referrals from ChatGPT or other LLMs.
- **Stochastic Outputs:**
LLMs may generate non-existent URLs or "hallucinate" sources. Always verify extracted links.
- **Streamlit App is Free to use outside this space:**
  No password-protected files or API has been leveraged so it's just free.


## 🛠️ LLM Data Extraction Bookmarklets

Expand your research to other LLMs using these bookmarklets:

### Perplexity Grounded Query Extractor

```javascript
javascript:(async()=>{const s=(location.pathname.match(/\/search\/([^/?#]+)/)||[])[1];if(s){const t=Date.now();const q=`with_parent_info=1&with_schematized_response=1&from_first=1&version=2.18&source=default&limit=100&offset=0&supported_block_use_cases=answer_modes&supported_block_use_cases=media_items&supported_block_use_cases=knowledge_cards&supported_block_use_cases=inline_knowledge_cards&_t=${t}`;const r=await fetch(`/rest/thread/${s}?${q}`,{credentials:'include',cache:'no-cache'});if(r.ok){const d=await r.json(),u=URL.createObjectURL(new Blob([JSON.stringify(d,null,2)]));Object.assign(document.createElement('a'),{href:u,download:`perplexity-${s}.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2e3);}}})();
```


### Claude Grounded Query Extractor

```javascript
javascript:(async()=>{try{const c=location.pathname.match(/\/chat\/([^/]+)/)?.[1];if(!c){alert('Open%20a%20Claude%20chat%20first');return;}const t=Date.now();const o=(await(await fetch(`/api/organizations?_t=${t}`,{credentials:'include',cache:'no-cache'})).json())[0].uuid;const j=await(await fetch(`/api/organizations/${o}/chat_conversations/${c}?tree=true&rendering_mode=messages&render_all_tools=true&_t=${t}`,{credentials:'include',cache:'no-cache'})).json();const u=URL.createObjectURL(new Blob([JSON.stringify(j,null,2)],{type:'application/json'}));Object.assign(document.createElement('a'),{href:u,download:`claude-${c}-rich.json`}).click();setTimeout(()=>URL.revokeObjectURL(u),2000);}catch(e){alert('Could%20not%20fetch%20rich%20conversation%20JSON');console.error(e);}})();
```


## 🔗 Link to the App 

- [ChatGPT Mentions Visualizer (Streamlit)](https://chatgpt-mentions-visualizer.streamlit.app/)
- [GitHub: ChatGPT Mentions Extractor](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/app.py)
