# LocoTiempo

This is possibly one of the most simple, sad and basic MCP servers out there, i am just practizing. 

This MCP server uses the Spanish Bureau of Meteorology (AEM, Agencia Espanola de Meteorologia) to provide a way to get 
the weather prediction for any of the provinces of Spain (there are 50 of those). 

The input is the name of the province in Spanish and the output will be the text, in Spanish, with the weather 
prediction. This requires an API key for the AEM Api, which can be obtained at https://opendata.aemet.es/centrodedescargas/inicio 

You need to define an environment variable named `AEM_API_KEY` for this to work. 

I have tested this with `fast-agent`, see

```

Last turn: 1,625 Input, 448 Output (1.0%) ^

default > What is the weather like in Badajoz?

▎▶ default ─────────────────────────────────────────────────────────────────────────────────────────[claude-sonnet-4-0 turn 4]

What is the weather like in Badajoz?                                                                                          

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


▎◀ default ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────

the assistant requested tool calls

─ [locotiempo] ───────────────────────────────────────────────────────────────────────────────────────────────────────────────


▎◀ default ─────────────────────────────────────────────────────────────────────────[tool request - locotiempo-get_prediction]

{'state': 'Badajoz'}

─ [get_predict…] ─────────────────────────────────────────────────────────────────────────────────────────────────────────────


▎▶ default ──────────────────────────────────────────────────────────────────────────────[tool result - Text Only (541 chars)]

AGENCIA ESTATAL DE METEOROLOGÍA
PREDICCIÓN PARA LA PROVINCIA DE BADAJOZ
DÍA 19 DE JULIO DE 2025 A LAS 14:01 HORA OFICIAL
PREDICCIÓN VÁLIDA PARA EL SÁBADO 19

BADAJOZ
Poco nuboso con algunos intervalos de nubes bajas a primeras
horas. Temperaturas con ligeros cambios. Viento del oeste, flojo a
moderado.

TEMPERATURAS MÍNIMAS Y MÁXIMAS PREV...

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


▎◀ default ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Here's the weather forecast for Badajoz province for Saturday, July 19th, 2025:                                               


                                                      General Forecast:                                                       

 • Sky: Partly cloudy with some low cloud intervals in the early hours                                                        
 • Temperatures: Slight changes compared to the previous day                                                                  
 • Wind: Westerly, light to moderate                                                                                          


                                          Expected Temperatures (Min and Max in °C):                                          

 • Badajoz: 16° - 33°                                                                                                         
 • Zafra: 14° - 32°                                                                                                           
 • Llerena: 16° - 31°                                                                                                         
 • Mérida: 15° - 33°                                                                                                          

The weather in Badajoz will be quite pleasant with partly cloudy skies and comfortable temperatures. Maximum temperatures will
range from 31-33°C, making it slightly warmer than Cáceres but similar overall conditions with westerly winds.                

─ [locotiempo] ───────────────────────────────────────────────────────────────────────────────────────────────────────────────


Last turn: 2,343 Input, 202 Output, 1 tool calls (1.3%) *

default >

```