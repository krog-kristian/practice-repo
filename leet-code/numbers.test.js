import { romanToInt } from './roman_to_int';

describe('romanToInt', () => {
  it('converts the first numeral', () => {
    const numeral = 'I';
    expect(romanToInt(numeral)).toEqual(1);
  });

  it('converts the second numeral', () => {
    const numeral = 'II';
    expect(romanToInt(numeral)).toEqual(2);
  });

  it('converts the third numeral', () => {
    const numeral = 'III';
    expect(romanToInt(numeral)).toEqual(3);
  });

  it('converts the fourth numeral', () => {
    const numeral = 'IV';
    expect(romanToInt(numeral)).toEqual(4);
  });

  it('converts the fith numeral', () => {
    const numeral = 'V';
    expect(romanToInt(numeral)).toEqual(5);
  });

  it('converts the sith numeral', () => {
    const numeral = 'VI';
    expect(romanToInt(numeral)).toEqual(6);
  });

  it('converts the seventh numeral', () => {
    const numeral = 'VII';
    expect(romanToInt(numeral)).toEqual(7);
  });

  it('converts the eigth numeral', () => {
    const numeral = 'VIII';
    expect(romanToInt(numeral)).toEqual(8);
  });

  it('converts the ninth numeral', () => {
    const numeral = 'IX';
    expect(romanToInt(numeral)).toEqual(9);
  });

  it('converts the tenth numeral', () => {
    const numeral = 'X';
    expect(romanToInt(numeral)).toEqual(10);
  });

  it('converts the fourteenth numeral', () => {
    const numeral = 'XIV';
    expect(romanToInt(numeral)).toEqual(14);
  });

  it('converts the 20th numeral', () => {
    const numeral = 'XX';
    expect(romanToInt(numeral)).toEqual(20);
  });

  it('converts the 31st numeral', () => {
    const numeral = 'XXXI';
    expect(romanToInt(numeral)).toEqual(31);
  });

  it('converts the 41st numeral', () => {
    const numeral = 'XLI';
    expect(romanToInt(numeral)).toEqual(41);
  });

  it('converts the 74th numeral', () => {
    const numeral = 'LXXIV';
    expect(romanToInt(numeral)).toEqual(74);
  });
});
