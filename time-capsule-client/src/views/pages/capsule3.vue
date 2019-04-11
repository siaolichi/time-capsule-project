<template>
    <div class="caption">
        <h3>Thumbnail label 3</h3>
        <p>...</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
    </div>
</template>
<script>
    export default {
        data(){
            return {}
        },
        created(){
            console.log(this.$route.params.id);
        }
    }
</script>