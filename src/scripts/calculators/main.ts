import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

function calculate_damage_coeff(e: any) {
    e.preventDefault();

    axios({
      method: 'post',
      url: '/calculators/damage_resistance',
      data: {
        damage: 'Fred',
        damage_resist: 'Flintstone'
      }
    }).then(function(response) {
      console.log(response.data);
    });
}

var damage_coeff_form = document.querySelector('form');
damage_coeff_form.onsubmit = calculate_damage_coeff;
