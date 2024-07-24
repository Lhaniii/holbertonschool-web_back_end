export default function guardrail(mathFunction) {
  const queu = [];
  try {
    const sum = mathFunction();
    queueMicrotask.push(sum);
  } catch (erro) {
    queu.push(`Error: ${error.message}`);
  } finally {
    queu.push('Guardrail was processed');
  }
  return queu;
}
