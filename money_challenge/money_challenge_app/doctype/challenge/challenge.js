// Copyright (c) 2018, littlehera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Challenge', {
	'refresh':function(frm){
        set_read_only_fields(frm);
	},
    'generated_iterations':function(frm){
	    set_read_only_fields(frm);
    },
	'challenger': function(frm) {
		update_name(frm);
	},
	'challenge_type': function(frm){
		update_name(frm);
	}
});

frappe.ui.form.on('Challenge', 'challenge_amount', function(frm){
	var challenge_amount = frm.doc.challenge_amount;
	if ((challenge_amount!="")&&(challenge_amount!="Custom")){
		frm.set_value("amount",challenge_amount);
	}
	else
		frm.set_value("amount",0);
});

frappe.ui.form.on("Challenge","validate",function(frm){
		frappe.call({
			method:"money_challenge.money_challenge_app.doctype.challenge.challenge.generate_weekly_cycles",
			args: {
				"challenge_scheme":frm.doc.challenge_scheme,
				"amount":frm.doc.amount,
				"generated_iterations": frm.doc.generated_iterations
			},
			callback:function(r){
				if(r.message){
					fill_cycle_table(frm, r.message);
				}
			}
		})
	});


function update_name(frm){
	var challenger = frm.doc.challenger;
	frappe.call({
		method : "frappe.client.get",
		args: {
			"doctype":"User",
			"name":challenger
		},
		callback: function(r){
			if(r.message){
				var challenge_name = r.message['first_name']+"'s "+frm.doc.challenge_type;
				frm.set_value('challenge_name', challenge_name)
			}
		}
	});
}

function fill_cycle_table(frm, message){
	var cycles = message;
	frm.clear_table("all_cycles");
	frm.refresh_field("all_cycles");
	for ( i = 0; i < cycles.length; i++){
		var newrow = frm.add_child("all_cycles");
		newrow.amount = cycles[i].amount;
		newrow.week = cycles[i].week;
		newrow.from_date = cycles[i].from_date;
		newrow.end_date = cycles[i].end_date;
	}
	for ( i = 0; i < cycles.length; i++){
		var newrow = frm.add_child("ongoing_cycles");
		newrow.amount = cycles[i].amount;
		newrow.week = cycles[i].week;
		newrow.from_date = cycles[i].from_date;
		newrow.end_date = cycles[i].end_date;
	}
	frm.refresh_field('all_cycles');
    frm.set_value("generated_iterations",1);
}

function set_read_only_fields(frm){
	if (frm.doc.generated_iterations=='1'){
		frm.set_df_property("challenger", "read_only",1);
		frm.set_df_property("challenge_scheme", "read_only",1);
		frm.set_df_property("challenge_amount", "read_only",1);
		frm.set_df_property("challenge_type", "read_only",1);
		frm.set_df_property("color", "read_only",1);
		}
	else{
		frm.set_df_property("challenger", "read_only",0);
		frm.set_df_property("challenge_scheme", "read_only",0);
		frm.set_df_property("challenge_amount", "read_only",0);
		frm.set_df_property("challenge_type", "read_only",0);
		frm.set_df_property("color", "read_only",0);
	}
}