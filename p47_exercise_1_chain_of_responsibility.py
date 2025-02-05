"""Chain of Responsibility – Zpracování zákaznické stížnosti
Vytvoř systém pro řešení zákaznických stížností,
kde požadavky postupně prochází řetězcem různých pracovníků
(např. asistent → manažer → ředitel).

Požadavky:
- Každá úroveň má svou třídu (Assistant, Manager, Director).
- Požadavky se předávají dál, dokud někdo problém nevyřeší.

Například: Asistent řeší jednoduché dotazy, manažer složitější a
ředitel ty nejvážnější."""