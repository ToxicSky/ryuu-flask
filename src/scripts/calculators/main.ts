import axios, { AxiosRequestConfig, AxiosPromise } from 'axios';

function calculate_damage_coeff(e: any) {
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
