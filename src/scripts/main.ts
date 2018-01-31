import {DamageCoeffCalculator} from './calculators/damage_coeff_calculator';

// var damage_coeff_form = document.querySelector('.damage_coeff_form');
var calc = new DamageCoeffCalculator();
console.log(calc);

// (function() {
//     var calc = new DamageCoeffCalculator();
//     // console.log(calc);
//     var damage_coeff_form = document.querySelector('.damage_coeff_form');
//     console.log(damage_coeff_form);
//     damage_coeff_form.addEventListener('submit', calc.calculate_damage_coeff);
// })();