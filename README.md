# Artficial Scientist

Searches for papers and data for a given topic, can specify time-period and quntity/quality, [inspiration](https://ai.gopubby.com/from-zero-to-genius-how-i-built-a-powerful-ai-agent-with-googles-adk-in-just-100-lines-of-code-79c16ceba7cc)  

# artsci cli
```
C:\users\animeshs\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\Scripts\adk run artsci
Log setup complete: C:\Users\animeshs\AppData\Local\Temp\agents_log\agent.20250513_110958.log
To access latest log: tail -F C:\Users\animeshs\AppData\Local\Temp\agents_log\agent.latest.log
Running agent topicfinding, type exit to exit.
[user]: 
[topicfinding]: I need a bit more information to help you effectively. Could you please specify the topic you're interested in, the types of resources you're looking for (papers, data, etc.), and when these resources should be created? Also, how many suggestions would you like, and what quality level are you aiming for (high, medium, or low)?

If you don't have a specific creation date in mind, would you like to use today's date (2025-05-13) or specify a preferred creation date?

[user]: what kind of research has been happening to study progression of MGUS to Myeloma since last year?
[topicfinding]: Okay, I can help you with that. Just to confirm, you're interested in research on the progression of MGUS to Myeloma.

To proceed, I need a bit more clarification:

*   **Types:** Are you interested in papers, data, or both?
*   **Creation Date:** You mentioned "last year." Would you like me to use 2024-05-13 as the start date for the research?
*   **Quantity:** How many paper and data suggestions would you like?
*   **Quality:** Are you looking for high, medium, or low-quality resources? If you don't specify, I'll default to high-quality.

[user]: both
[topicfinding]: Okay, great. Just to confirm, you're interested in research on the progression of MGUS to Myeloma, including both papers and data.

To proceed, I still need to confirm a few details:

*   **Creation Date:** You mentioned "last year." Would you like me to use 2024-05-13 as the start date for the research?
*   **Quantity:** How many paper and data suggestions would you like?
*   **Quality:** Are you looking for high, medium, or low-quality resources? If you don't specify, I'll default to high-quality.

[user]: show me top 10
[topicfinding]: Okay, just to confirm, you're interested in the following:

*   **Topic:** Research on the progression of MGUS to Myeloma
*   **Types:** Both papers and data
*   **Creation Date:** You mentioned "last year." Would you like me to use 2024-05-13 as the start date for the research?
*   **Quantity:** Top 10 suggestions (I'll assume 5 papers and 5 data suggestions)
*   **Quality:** High (default)

Please confirm if this is correct or if you would like to change any of these preferences.

[user]: yes
[user]: yes
[papers_agent]: Okay, I will find the top 5 high-quality papers related to the progression of MGUS to Myeloma, created after 2024-05-13.

[user]: yes
[data_agent]: Okay, I will find the top 5 high-quality datasets related to the progression of MGUS to Myeloma, created after 2024-05-13.

[user]: yes
[data_agent]: I am sorry, I cannot fulfill you request. I cannot search for the datasets with the current API.
```

# [artsci web](http://localhost:8000/dev-ui?app=agent)

```
C:\users\animeshs\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\Scripts\adk web  
C:\users\animeshs\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\Scripts\adk web
INFO:     Started server process [28840]
INFO:     Waiting for application startup.

+-----------------------------------------------------------------------------+
| ADK Web Server started                                                      |
|                                                                             |
| For local testing, access at http://localhost:8000.                         |
+-----------------------------------------------------------------------------+

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

![Image](https://github.com/user-attachments/assets/7a4c8d1d-0a31-473e-adf5-199ba10088af)

## test
What kind of research is available for MGUS since last year?


# issues

enable developer mode in windows https://stackoverflow.com/questions/69427548/flutter-pub-get-a-required-privilege-is-not-held-by-the-client/69735375#69735375 for cli to work
