# LLM Brand Authority \& Citation Analysis Toolkit

Analyze your brand's authority and citation patterns across leading Large Language Model (LLM) search engines. This toolkit helps you track backlinks, traffic sources, and reference behaviors from LLM-generated content.

## 🚀 Use Cases

- **Analyze brand authority** over LLM search engines
- **Track backlink proportions** from deep LLM conversations
- **Identify traffic channels** most referenced by LLMs for citations


## 📝 Data Preparation

Before uploading your data, follow these steps for a clean, standardized input:

1. **Consolidate Columns:**
Ensure your spreadsheet has a single tab with the following headers:
    - `Prompt`
    - `Content`
    - `Assitional Info`
2. **Header Adjustments:**
    - Replace any `Type` header with `Prompt` (this should contain the exact prompt used for LLM research).
    - Remove the `timestamp` column.
    - Optionally remove top rows containing grounded/normalized queries from the prompt.
3. **Example Table**


| Prompt | Content | Assitional Info |
| :-- | :-- | :-- |
| "Find brand mentions" | "Our brand is cited on example.com and xyz.net" | "ChatGPT, 2025-06-25" |


## 📊 How It Works

- **Upload XLSX file:**
The app generates a heatmap, with the Y-axis showing link occurrences by traffic referral source.
- **Source Classification:**
Link sources are classified using rule-based logic and labeled accordingly.
- **Live Data Updates:**
Enter your domain in the search bar to update the heatmap and data summaries in real time.


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


## 🐍 JSON to CSV Conversion (Python)

If your LLM exports are in JSON, convert them to CSV for analysis:

```python
import pandas as pd
import json

with open('perplexity-export.json') as f:
    data = json.load(f)

# Adjust this extraction logic based on JSON structure
df = pd.json_normalize(data['conversations'])
df.to_csv('output.csv', index=False)
```


## ⚠️ Caveats \& Notes

- **Attribution Issues:**
Some analytics platforms (e.g., GA4) may not accurately report traffic referrals from ChatGPT or other LLMs.
- **Stochastic Outputs:**
LLMs may generate non-existent URLs or "hallucinate" sources. Always verify extracted links.
- **Streamlit App is Free to use outside this space:**
  No password-protected files or API has been leveraged so it's just free.


## 🔗 Link to the App 

- [ChatGPT Mentions Visualizer (Streamlit)](https://chatgpt-mentions-visualizer.streamlit.app/)
- [GitHub: ChatGPT Mentions Extractor](https://github.com/simodepth96/ChatGPT-Mentions-Extractor/blob/main/app.py)
