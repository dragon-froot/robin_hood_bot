<template>
    <div class="card " style="width: 16em; margin: 2%" >
        <!-- <img class="card-img-top" src="" alt="Card image cap"> -->
        <div class="card-body" style="border-bottom: 1px solid #232323">
            <h5 class="card-title">{{ symbol }}</h5>
            <!-- <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p> -->
        </div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item">Average Buy Price: ${{ average_buy_price }}</li>
                <li class="list-group-item">Current Price: ${{ current_price }}</li>
                <li class="list-group-item">Current Equity: ${{ current_equity }}</li>
                <li class="list-group-item">Full Price Paid: ${{ price_paid }}</li>
                <li class="list-group-item">Quantity: {{ quantity }}</li>
            </ul>
        <!-- <div class="card-body">
            <a href="#" class="card-link">Card link</a>
            <a href="#" class="card-link">Another link</a>
        </div> -->
    </div>
</template>

<script>
export default {
    name: 'stock-card',
    props: {
        symbol: String,
        current_price: String,
        average_buy_price: String,
        current_equity: Number,
        price_paid: Number,
        quantity: String
    },
    data(){
        return {

        }
    }
}
</script>