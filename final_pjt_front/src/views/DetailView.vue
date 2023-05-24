<template>
  <div>
      <!-- 좋아요 버튼 -->
      <div class="like">
          <a class="heart-button" @click="[movieLike(), getMovieLike(), getMovieLikeCount()]">
              <i class="heart" :class="liked ? 'bi bi-suit-heart-fill' : 'bi bi-suit-heart'"></i>
          </a> 
          <p class="like-letter">좋아요 : {{ likes_count }}</p>
      </div>

    <!-- 하위 컴포넌트 -->
    <DetailMovie :movie=movies[movieId-1] />

    <!-- 댓글 입력 창 -->
    <div class="cmt">
        <h2 class="comment"><i class="bi-chat-right-text-fill"></i> 댓글</h2>
            <form class="inner" @submit.prevent="addComment" v-if="$store.state.token">
                <textarea class="textarea" v-model="newCommentText" placeholder="" style="width: 50%;"></textarea>
                <button class="w-btn w-btn-gra1" type="submit">댓글 달기</button>
            </form>
            

        <!-- 댓글 데이터 -->
        <MovieComment v-for = "comment in comments"
        :key="comment.id"
        :comment="comment" 
        @comment-deleted="deleteComment"
        />
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import DetailMovie from '@/components/DetailMovie.vue'
import MovieComment from '@/components/MovieComment.vue'

// import SignInView from '@/views/SignInView.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'DetailView',
    components: {
        DetailMovie,
        MovieComment,
    },
    created() {
        this.getMovieDetail()
        this.getComments()
        this.getMovieLike()
        this.getMovieLikeCount()
    },
    data() {
        return {
            movieId : this.$route.params.id,
            comments : [],
            newCommentText: '',
  
            // 추가
            likes_count: 0,
            liked: false,
        }
    },
    computed: {
        movies() {
              return this.$store.state.movies
        }
    },
    methods: {
        getMovieDetail() {
            axios({
                method: 'get',
                url: `${API_URL}/api/v1/movies/${this.movieId}/`,
            })
            .then(() => {
                // console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },

        getComments() {
            axios({
                method: 'get',
                url: `${API_URL}/api/v1/movies/${this.movieId}/comments/`,
            })
            .then((res) => {
                // console.log(res)
                const comments = res.data
                this.comments = comments
            })
            .catch((err) => {
                console.log(err)
            })
        },

        addComment() {
            const movieId = this.movieId
            const content = this.newCommentText  
            const data = {
                movie: movieId,
                content: content
            }
            axios({
                method: 'post',
                url:`${API_URL}/api/v1/movies/${this.movieId}/comments/`,
                data: data,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`
                }
            })
            .then((res) => {
                // console.log(res)
                this.comments.push(res.data)
                this.newCommentText = ''
            })
            .catch((err) => {
                console.log(err)
            })
        },

        deleteComment(deletedCommentId) {
            this.comments = this.comments.filter(comment => comment.id !== deletedCommentId)
        },

        movieLike() {
            if (!this.$store.state.token) {
                this.$router.push({ name: 'SignInView' })
                return
            }

            axios({
                method: 'post',
                url: `${API_URL}/api/v1/movies/${this.movieId}/like/${this.$store.state.username}/`,
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                },
            })
            .then(() => {
                this.getMovieLike();
                this.getMovieLikeCount();
            })     
            .catch((err) => {
                console.log(err);
            });
        },

        getMovieLike() {
            if (this.$store.state.username) {
                axios({
                    method: 'get',
                    url: `${API_URL}/api/v1/movies/${this.movieId}/liked/users/${this.$store.state.username}/`,
                })
                .then((res) => {
                    this.liked = res.data.liked;
                    // console.log(res.data);
                })
                .catch((err) => {
                    console.log(err);
                });
            } else {
                this.liked = false;
            }
        },


        getMovieLikeCount() {
            axios({
            method:'get',
            url:`${API_URL}/api/v1/movies/${this.movieId}/liked/counts/`,
            })
            .then((res) => {
                // console.log(res)
                this.likes_count = res.data.likes_count
                // console.log(res.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
    }
}
</script>

<style scoped>
.comment {
  color: rgb(153, 78, 153);
  font-family: 'Black Han Sans', sans-serif;
  margin-top: 50px;
}

.textarea {
    border-radius: 20px;
    border: 2px solid rgb(196, 104, 196);
    display: inline;
    margin: 7px;
}

.heart {
    color: rgb(202, 34, 202);
    font-size: 30px;
    padding: 10px;
}

.cmt {
    margin-bottom: 70px;
}

.like {
    display: flex;
    margin-left: 50px;
    margin-top: 30px;
}

.like-letter{
    margin-top: 13px;
    font-weight: bold; 
    color: rgb(153, 78, 153);
}

.w-btn-gra1 {
    background: linear-gradient(-45deg, #33ccff 0%, #ff99cc 100%);
    color: white;
    border-radius: 10px;
    /* border-color: aliceblue; */
    border-color: rgb(196, 104, 196);
    padding: 10px;
    /* margin-top: 10px; */
    display: inline;
}

.textarea, .w-btn {
    vertical-align: middle;
}


</style>