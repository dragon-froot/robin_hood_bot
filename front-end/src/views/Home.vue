<template>
  <div class="container-fluid ">
      <h1>Equity</h1>
      <div class="d-flex flex-wrap ">
              <StockCard v-for="item in holdings"
               :key="item.symbol"
               :symbol="item.symbol"
               :current_price="item.current_price"
               :average_buy_price="item.average_buy_price"
               :current_equity="item.current_equity"
               :price_paid="item.price_paid"
               :quantity="item.quantity" />
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import StockCard from '../components/StockCard.vue'

export default {
  name: 'Home',
  components: {
    StockCard
  },
  data(){
    return {
      holdings: []
    }
  }, 
  mounted() {
    let base = 'http://127.0.0.1:5000/'
    axios.get(base).then(res => {
      this.holdings = res.data
    }).catch(err => console.log(err))
  }
}
</script>
