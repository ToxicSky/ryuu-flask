import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

export function calculate_damage_coeff(e: any) {
    e.preventDefault();

    axios({
      method: 'post',
      url: '/api/calculators/damage_resistance',

      data: {
        damage: 100,
        damage_resist: 50
      }
    }).then(function(response) {
      console.log(response.data);
    });
}

var damage_coeff_form = <HTMLElement>document.body.querySelector('form');
damage_coeff_form.addEventListener('submit', calculate_damage_coeff);
