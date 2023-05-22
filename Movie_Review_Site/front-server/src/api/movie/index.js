import api from '@/api/base'

const fetchMovies = async ()=>{
    return api.get('/movies/')
}

const fetchSearchMovies = async ({title})=>{

    return api({
        method:'get',
        url:'/movies/search/',
        params:{
            title : title, 
        }
    })
}

const getMovie_Detail = async(params_id)=>{
    return api.get(`/movies/${params_id}/`)
}

const WishList = async({movie_id})=>{
    console.log(movie_id)
    return api.post(`/movies/${movie_id}/wishlist/`)
}

const MyWishList = async({user_name}) => {
    console.log("에효",user_name)
    return api.get(`/accounts/my_wishlist/${user_name}/`)
}
export { fetchMovies, getMovie_Detail, fetchSearchMovies, WishList, MyWishList}