export default function appendToEachArrayValue(array, appendString) {
  const NewAr = [];

  for (const idx of array) {
    NesAr.push(appendString + idx);
  }
  
  return NewAr;
}
