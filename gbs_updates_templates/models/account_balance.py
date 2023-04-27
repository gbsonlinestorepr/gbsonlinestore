from datetime import datetime

from odoo import models


class ReportTrialBalance(models.AbstractModel):
    _inherit = 'report.account.report_trialbalance'

    def _get_accounts(self, accounts, display_account):
        data_ids = super(ReportTrialBalance, self)._get_accounts(accounts, display_account)
        tables, where_clause, where_params = self.env['account.move.line']._query_get()
        fiscalyear_last_day = self.env.user.company_id.fiscalyear_last_day
        fiscalyear_last_month = self.env.user.company_id.fiscalyear_last_month
        string_fiscal_year_start = "%s-%s-%s" % (datetime.today().year - 1,
                                                 fiscalyear_last_month,
                                                 fiscalyear_last_day)
        string_fiscal_year_end = "%s-%s-%s" % (datetime.today().year,
                                               fiscalyear_last_month,
                                               fiscalyear_last_day)
        if (len(where_params) > 2):
            where_params.pop(0)
        tables = tables.replace('"', '')

        if not tables:
            tables = 'account_move_line'
        wheres = [""]
        where_clause = where_clause.replace('AND  ("account_move_line"."date" >= %s)', '').replace('<=', '<')
        if where_clause.strip():
            wheres.append(where_clause.strip())
        filters = " AND ".join(wheres)
        request = ("SELECT account_id AS id, (SUM(debit) - SUM(credit)) AS open_balance " + \
                   " FROM " + tables + " WHERE account_id IN %s " + filters + " GROUP BY account_id")
        params = (tuple(accounts.ids),) + tuple(where_params)

        self.env.cr.execute(request, params)

        account_result = {}
        for row in self.env.cr.dictfetchall():
            account_result[row['id']] = row
        account_res = {}

        # date_to = string_fiscal_year_end

        if len(where_params) > 1:
            # move_ids = self.env['account.move.line'].search([('account_id', 'in', accounts.ids),
            #                                                  ('move_id.state', '=', 'posted'),
            #                                                  ('date', '>', string_fiscal_year_start),
            #                                                  ('date', '<', date_to)])

            for account in accounts:
                if account.id in account_result:
                    account_res[account.code] = account_result[account.id].get('open_balance')

        for data_id in data_ids:
            data_id.update({'open_balance': account_res.get(data_id.get('code'), 0.0),
                            'net_balance': account_res.get(data_id.get('code'), 0.0) + data_id.get('balance')})
            # account_id = self.env['account.account'].search([('code','=',data_id.get('code'))])
            # if not account_id.user_type_id.include_initial_balance:
            #     data_id.update({'open_balance': 0.0})
            # else:
            #     data_id.update({'open_balance': sum(
            #         move_ids.filtered(lambda x: x.account_id.code == data_id.get('code')).mapped('balance'))})

            # if data_id.get('code') in account_res:
            #     data_id.update({'net_balance': account_res[data_id.get('code')] + data_id.get('balance')})
            # else:
            #     data_id.update({'net_balance': data_id.get('balance')})
        return data_ids
