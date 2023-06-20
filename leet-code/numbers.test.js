import { romanToInt } from './roman_to_int';

describe('romanToInt', () => {
  it('converts the first numberal', () => {
    const firstNumeral = 'I';
    expect(romanToInt(firstNumeral)).toEqual(1);
  });
});
