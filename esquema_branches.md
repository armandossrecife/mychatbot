# Controle de Branches

## Devs integrando issues no branch de desenvolvimento

```bash
gitGraph
   commit id: "init repository"
   commit id: "Frameworks e Libs"
   branch desenvolvimento
   branch issue_1
   branch issue_2
   branch issue_3
   branch issue_N
   checkout issue_1
   commit id: "F1"
   commit id: "F2"
   commit id: "Testes de Integração (F1,F2)"
   checkout desenvolvimento
   merge issue_1 id: "Integra F1 e F2"
   commit id: "Resolve conflitos issue_1"
   checkout issue_2
   commit id: "F3"
   commit id: "F4"
   commit id: "Testes de Integração (F3,F4)"
   checkout desenvolvimento
   merge issue_2 id: "Integra F1,F2,F3 e F4"
   commit id: "Resolve conflitos issue_2"
   checkout issue_3
   commit id: "F5"
   commit id: "F6"
   commit id: "Testes de Integração (F5,F6)"
   checkout desenvolvimento
   merge issue_3 id: "Integra F1,F2,F3,F4,F5 e F6"
   commit id: "Resolve conflitos issue_3"
   commit id: "Testes de Integração (F1,..,F6)"
   commit id: "Testes de Sistema"
   commit id: "Prototipo1"
   checkout main
   merge desenvolvimento id: "Integra as Funcionalidades (F1,...,F6)"
   commit id: "Release 1.0.0" tag: "v1.0.0"
```
https://mermaid.js.org/syntax/gitgraph.html

O diagrama resultante é: 

![Esquema de branches!](https://raw.githubusercontent.com/armandossrecife/mychatbot/main/esquema_branches.png) "Branches: main, desenvolvimento, dev1, dev2 e dev3"
