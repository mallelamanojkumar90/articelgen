# Deploying to Render

This guide will help you deploy the CrewAI Article Generator to Render.

## Prerequisites

- GitHub account
- Render account (free tier available at [render.com](https://render.com))
- OpenAI API key

## Step-by-Step Deployment

### 1. Prepare Your Repository

Make sure all files are committed to Git:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Create a Render Account

1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Authorize Render to access your repositories

### 3. Deploy the Application

#### Option A: Using render.yaml (Recommended)

1. In Render dashboard, click **"New +"** → **"Blueprint"**
2. Connect your GitHub repository
3. Render will automatically detect `render.yaml`
4. Click **"Apply"**

#### Option B: Manual Setup

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `crewai-article-generator` (or your choice)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: `Free`

### 4. Set Environment Variables

1. In your service dashboard, go to **"Environment"**
2. Add the following environment variable:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your OpenAI API key
3. Click **"Save Changes"**

### 5. Deploy

1. Render will automatically build and deploy your app
2. Wait for the build to complete (2-5 minutes)
3. Once deployed, you'll get a URL like: `https://crewai-article-generator.onrender.com`

## Important Notes

### Free Tier Limitations

- ⏱️ **Spin down after 15 minutes of inactivity**
  - First request after spin down takes 30-60 seconds to wake up
  - Consider upgrading to paid plan for always-on service
  
- 💾 **512 MB RAM limit**
  - Should be sufficient for this application
  
- 🔄 **Monthly build minutes limit**
  - Free tier includes 750 hours/month

### Production Considerations

1. **Long-Running Tasks**
   - Article generation can take 2-5+ minutes
   - Render's free tier supports this (unlike Vercel)
   - Consider adding a timeout message in the UI

2. **In-Memory Storage**
   - Current implementation uses in-memory task storage
   - Tasks are lost if the service restarts
   - For production, consider using Redis or a database

3. **CORS Configuration**
   - Already configured with Flask-CORS
   - Update if you need specific domain restrictions

## Monitoring

1. **Logs**: View real-time logs in Render dashboard under "Logs"
2. **Metrics**: Monitor CPU, memory, and bandwidth usage
3. **Alerts**: Set up email alerts for service issues

## Troubleshooting

### Build Fails

**Exit Status 127 (Command Not Found):**
- This usually means gunicorn isn't found
- **Solution**: Updated `render.yaml` to use `python -m gunicorn` instead of just `gunicorn`
- Verify `requirements.txt` includes `gunicorn>=21.0.0`
- Check build logs for pip installation errors

**Other Build Errors:**
- Check that `requirements.txt` is up to date
- Verify Python version in `runtime.txt` matches your local version
- Review build logs for specific errors

### Service Won't Start

- Verify `OPENAI_API_KEY` is set correctly
- Check start command is `gunicorn app:app`
- Review application logs for errors

### Slow First Request

- This is normal for free tier (spin down after inactivity)
- Upgrade to paid plan for always-on service
- Or use a service like UptimeRobot to ping your app periodically

### Article Generation Timeout

- Ensure your OpenAI API key has sufficient credits
- Check logs for CrewAI errors
- Verify network connectivity to OpenAI API

## Updating Your Deployment

Render automatically deploys when you push to your main branch:

```bash
git add .
git commit -m "Update application"
git push origin main
```

Render will detect the push and redeploy automatically.

## Custom Domain (Optional)

1. Go to **"Settings"** → **"Custom Domain"**
2. Add your domain
3. Update DNS records as instructed
4. Render provides free SSL certificates

## Cost Optimization

**Free Tier:**
- Perfect for testing and personal projects
- Spins down after 15 minutes of inactivity

**Starter Plan ($7/month):**
- Always-on service
- No spin down delays
- Better for production use

## Next Steps

After deployment:
1. Test article generation with a simple topic
2. Monitor logs for any errors
3. Share your deployed URL!
4. Consider upgrading for production use

---

**Your app is now live! 🎉**

Access it at: `https://your-service-name.onrender.com`
