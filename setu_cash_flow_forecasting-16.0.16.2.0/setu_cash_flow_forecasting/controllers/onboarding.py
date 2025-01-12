from odoo import http
from odoo.http import request


class OnboardingController(http.Controller):

    @http.route('/setu_cash_flow_forecasting/cash_dashboard_onboarding', auth='user', type='json')
    def cash_dashboard_onboarding(self):
        """ Returns the `banner` for the cash forecasting dashboard onboarding panel.
            It can be empty if the user has closed it or if he doesn't have
            the permission to see it. """
        company = request.env.company

        if not request.env.is_admin() or \
                company.cash_dashboard_onboarding_state == 'closed':
            return {}

        return {
            'html': request.env['ir.qweb']._render('setu_cash_flow_forecasting.cash_dashboard_onboarding_panel', {
                'company': company,
                'state': company.get_and_update_cash_dashboard_onboarding_state()
            })
        }
