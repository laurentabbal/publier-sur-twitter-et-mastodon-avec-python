#== CONNEXION TWITTER ==========================================================
import tweepy

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

twitterv1 = tweepy.API(tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret))
twitterv2 = tweepy.Client(consumer_key=api_key, consumer_secret=api_key_secret, access_token=access_token, access_token_secret=access_token_secret)
#===============================================================================

#== CONNEXION MASTODON =========================================================
from mastodon import Mastodon

mastodon_token = ""
mastodon_url = ""

mastodon = Mastodon(access_token = mastodon_token, api_base_url = mastodon_url)
#===============================================================================

text  = "Test #Python pour publier simultanément sur #Twitter et #Mastodon (texte + image). Avantage: plus besoin de passer par http://crossposter.masto.donte.com.br (ou équivalent) et donc plus besoin de partager des paramètres de connexion avec des sites tiers."
image = "piou.png"

# Chargement de l'image sur Twitter
media_twitter = twitterv1.media_upload(image)

# Chargement de l'image sur Mastodon
media_mastodon = mastodon.media_post(image)

# Envoi sur Twitter
twitterv2.create_tweet(text=text, media_ids=[media_twitter.media_id])

# Envoi sur Mastodon
mastodon.status_post(text, media_ids=[media_mastodon.id])
