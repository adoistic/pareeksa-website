/**
 * Cloudflare Worker: Contact Form & Demo Request Email Backend
 * 
 * This is a boilerplate script for a Cloudflare Worker that processes form submissions
 * from your website, validates the fields, and forwards the details to corp@pareeksa.com
 * using an email service like SendGrid, Mailgun, or Cloudflare Email Routing.
 * 
 * To deploy:
 * 1. Install wrangler: npm install -g wrangler
 * 2. Run 'wrangler login' and 'wrangler init demo-form-backend'
 * 3. Replace the worker script with this content
 * 4. Configure environment variables (e.g. SENDGRID_API_KEY) in wrangler.toml or dashboard
 * 5. Run 'wrangler deploy'
 * 6. Update the 'action' attribute of the forms in index.html, brand.html, and tools/build_services.py
 *    to your deployed Cloudflare Worker URL.
 */

export default {
  async fetch(request, env) {
    // Handle CORS preflight request
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Max-Age": "86400"
        }
      });
    }

    if (request.method !== "POST") {
      return new Response(JSON.stringify({ error: "Method not allowed" }), {
        status: 405,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }

    try {
      const payload = await request.json();
      const { name, phone, email, organization, message, selected_service, submission_time, subject } = payload;

      // 1. Server-side Validation
      if (!name || name.trim() === "") {
        return new Response(JSON.stringify({ error: "Name is required." }), {
          status: 400,
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
        });
      }
      if (!phone || phone.trim() === "" || phone.replace(/[^0-9+]/g, "").length < 10) {
        return new Response(JSON.stringify({ error: "A valid mobile number is required." }), {
          status: 400,
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
        });
      }
      const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!email || !emailRegex.test(email.trim())) {
        return new Response(JSON.stringify({ error: "A valid email address is required." }), {
          status: 400,
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
        });
      }

      // 2. Format the email body
      const emailSubject = subject || `New Demo Request – ${selected_service || "General Inquiry"} – ${name}`;
      const emailBody = `
New Request Received
--------------------
Name: ${name.trim()}
Mobile: ${phone.trim()}
Email: ${email.trim()}
Institute / Organization: ${organization ? organization.trim() : "Not Provided"}
Message: ${message ? message.trim() : "Not Provided"}

Context details:
--------------------
Selected Service: ${selected_service || "General Inquiry (Homepage)"}
Submission Time: ${submission_time || new Date().toISOString()}
      `.trim();

      // 3. Send Email (Example using SendGrid API)
      // You must add SENDGRID_API_KEY to your environment variables (wrangler secret put SENDGRID_API_KEY)
      const sendGridKey = env.SENDGRID_API_KEY;
      if (!sendGridKey) {
        console.error("Missing SENDGRID_API_KEY environment variable.");
        // Fallback for testing: log to console
        console.log("Email body:\n", emailBody);
        return new Response(JSON.stringify({ 
          success: true, 
          message: "[Dry-run Mode] Form is valid. Deployed worker is missing SENDGRID_API_KEY secret."
        }), {
          headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
        });
      }

      const emailResponse = await fetch("https://api.sendgrid.com/v3/mail/send", {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${sendGridKey}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          personalizations: [
            {
              to: [{ email: "corp@pareeksa.com" }],
              subject: emailSubject
            }
          ],
          from: { email: "no-reply@pareeksa.com", name: "Pareeksa Forms" },
          content: [
            {
              type: "text/plain",
              value: emailBody
            }
          ]
        })
      });

      if (!emailResponse.ok) {
        const errorText = await emailResponse.text();
        throw new Error(`SendGrid API error: ${errorText}`);
      }

      return new Response(JSON.stringify({ success: true, message: "Request sent successfully!" }), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });

    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      });
    }
  }
};
