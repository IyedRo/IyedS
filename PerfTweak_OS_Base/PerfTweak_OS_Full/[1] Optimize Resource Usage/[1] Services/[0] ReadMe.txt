1. Windows Update - `wuauserv`
2. Windows Search - `WSearch`
3. SysMain - `SysMain`
4. Microsoft Passport - `UsoSvc`
5. User Experience Virtualization Service - `UEV`
6. Downloaded Maps Manager - `MapsBroker`
7. Background Intelligent Transfer Service - `BITS`
8. Retail Demo Service - `RetailDemo`
9. Microsoft Account Sign-in Assistant - `wlidsvc`
10. Windows Error Reporting Service - `WerSvc`
11. Windows Update Medic Service - `WaaSMedicSvc`
12. Windows Update Orchestrator Service - `UsoSvc`
sc stop wuauserv
sc config wuauserv start= disabled
sc stop WSearch
sc config WSearch start= disabled
sc stop SysMain
sc config SysMain start= disabled
sc stop UsoSvc
sc config UsoSvc start= disabled
sc stop UEV
sc config UEV start= disabled
sc stop MapsBroker
sc config MapsBroker start= disabled
sc stop BITS
sc config BITS start= disabled
sc stop RetailDemo
sc config RetailDemo start= disabled
sc stop wlidsvc
sc config wlidsvc start= disabled
sc stop WerSvc
sc config WerSvc start= disabled
sc stop WaaSMedicSvc
sc config WaaSMedicSvc start= disabled