html = """

<div class="f-g2">
          <!----><div class="d-flex" ng-if="lotDetails.lotId">
            <!--Lot Number-->
            <label for="LotNumber" data-uname="lotdetailLotNumber" class="bold">
              Lot Number:
            </label>
            <span id="LotNumber" class="lot-details-desc d-f bold" data-uname="lotdetailVinvalue">
              37980214

              <span class="ml-5">
                <!----><a target="_blank" ng-if="!lotDetails.hcvu" ng-click="getClearVinURL();" title="Click for ClearVin Report" data-uname="lotdetailInstavinlink" check-for-logged-in-user="">
                  <!----><img ng-if="lotDetails.fv" src="../images/lot-details/lot-details-sprite.svg" alt="ClearVin Report" class="img-responsive clear-vin-history"><!---->
                </a><!---->
                <!----><a target="_blank" ng-if="!lotDetails.hevu" ng-click="getEpicVinURL();" title="Click for EpicVin Report" data-uname="lotdetailInstavinlink" check-for-logged-in-user="">
                  <!----><img ng-if="lotDetails.fv" src="../images/lot-details/lot-details-sprite.svg" class="img-responsive vin-history" alt="Vin History Report"><!---->
                </a><!---->
              </span>
            </span>
          </div><!---->

          <!----><div ng-if="lotDetails.fv">
            <!----><div ng-if="!ukVinNumber">
              <!--VIN Number-->
              <div class="pt-8 d-flex border-top-gray">
                  <label for="VIN:" data-uname="lotdetailVin" class="bold">
                    VIN:
                  </label>
                  <div masking="" number="5UXKU6C59G0******" lot-number="37980214" field="fv"><!---->

<!----><span ng-if="unmaskingDisabled">
    <span class="lot-details-desc">
       5UXKU6C59G0******
    </span>
</span><!----></div>
              </div>
            </div><!---->
          </div><!---->

          <div></div>

          <!----><div class="pt-8 d-flex border-top-gray" ng-if="lotDetails.ts || lotDetails.td">
            <!--Doc Type-->
            <label for="SaleTitleDescription" data-uname="lotdetailTitledescription" class="bold">
              Title Code:
            </label>
            <span class="lot-details-desc w100" data-uname="lotdetailTitledescriptionvalue">
              <!----><span class="bold d-flex j-c_s-b" ng-if="lotDetails.ts | trim">
                <span>
                  LA - CERTIFICATE OF TITLE
                  <!----><a ng-if="titlePendingTooltipMsg" data-uname="titlePendingToolTip" href="javascript:void(0)" data-placement="auto right" data-toggle="popover" data-content="(P) = Title is Pending from Seller and will be provided with in 30 days" tooltip="" data-original-title="" title="">
                    (P)
                  </a><!---->
                </span>
                <a data-uname="lotdetailDoctypetooltip" class="right" href="javascript:void(0)" data-placement=" auto right" data-toggle="popover" data-content="CERTIFICATE OF TITLE without brands. This is commonly     referred to as a Clean or Clear Title. / Title Group: Clean" aria-label="Lot Detail Doc Type Tooltip" tooltip="" data-original-title="" title="">
                  <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
                </a>
              </span><!---->
            </span>
          </div><!---->

          
          <!----><div ng-if="lotDetails.orr !== undefined || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <!--Odometer-->
              <label for="Odometer:" data-uname="lotdetailOdometer" class="bold">
                Odometer:
              </label>
              <span class="lot-details-desc odometer-value w100" data-uname="lotdetailOdometervalue">
                <!----><span ng-if="(lotDetails.ord | trim)!=''" class="bold d-flex j-c_s-b">
                  <span>
                    111,172 mi&nbsp;(ACTUAL)
                  </span>
                  <a data-uname="lotdetailOdometertooltip" data-toggle="popover" popoverid="odometer-content" class="popover-span right" aria-label="Lot Detail Odometer Tooltip" tooltip="" data-original-title="" title="">
                    <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
                  </a>
                </span><!---->
                <!---->
              </span>
            </div>
          </div><!---->

          <div></div>

          <div>
            <!-- Present only for GStack region sites -->
          </div>

          <!---->

          
            <!----><div ng-if="(!showCopartSelectCode &amp;&amp; (lotDetails.dd | trim)!='') || !hideEmptyFields" class="pt-8 d-flex border-top-gray">
              <!--Primary Damage-->
              <label data-uname="lotdetailPrimarydamage" class="bold">
                Primary Damage:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailPrimarydamagevalue">
                MINOR DENT/SCRATCHES
              </span>
            </div><!---->
          

          
            <!---->
          
          

          <!--Estimated Retail Value-->
          <!---->

          <!----><div ng-if="(lotDetails.cy | trim)!='' &amp;&amp; hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <!--Cylinders-->
              <label data-uname="lotdetailCyllinder" class="bold">
                Cylinders:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailCylindervalue">
                8
              </span>
            </div>
          </div><!---->

          <!---->

          <div>
            <!---->
          </div>

          <div>
            <!-- Present only for GStack region sites -->
          </div>

          <div></div>

          <div></div>

          <!----><div ng-if="(lotDetails.bstl | trim)!='' || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray clr">
              <!--Body Style-->
              <label data-uname="lotdetailBodystyle" class="bold">
                Body Style:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailBodystylevalue">
                4DR SPOR
              </span>
            </div>
          </div><!---->

          <!----><div ng-if="(lotDetails.clr | trim)!='' || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <label data-uname="lotdetailColor">
                Color:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailColorvalue">
                BURGUNDY
              </span>
            </div>
          </div><!---->

          <!---->

          <!----><div ng-if="(lotDetails.egn | trim)!=''">
            <div class="pt-8 d-flex border-top-gray">
              <!--Engine Type-->
              <label data-uname="lotdetailEngine" class="bold">
                Engine Type:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailEnginetype">
                4.4L  8
              </span>
            </div>
          </div><!---->

          <!---->

          <div>
            <!----><div ng-if="lotDetails.tmtp || lotDetails.htsmn=='Y'" class="d-flex pt-5 border-top-gray">
                <label data-uname="">
                    Transmission:
                </label>
                <span class="lot-details-desc" data-uname="">
                    AUTOMATIC
                </span>
            </div><!---->
            <!---->
        </div>

          <!----><div ng-if="(lotDetails.drv | trim)!='' || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <!--Drive-->
              <label data-uname="lotdetailDrive" class="bold">
                Drive:
              </label>
              <span class="lot-details-desc" data-uname="DriverValue">
                All wheel drive
              </span>
            </div>
          </div><!---->

          <!----><div ng-if="vehicleTypeDesc &amp;&amp; lotDetails.vehTypDesc" lot-data-if="AUTOMOBILE">
            <div class="pt-8 d-flex border-top-gray">
              <label data-uname="lotdetailvehicletype">
                Vehicle Type:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailvehicletype">
                AUTOMOBILE
              </span>
            </div>
          </div><!---->

          <div>
            <!-- Engine Power Present only for GStack region sites -->
          </div>

          <div>
            <!-- CO2 Emission Present only for GStack region sites -->
          </div>

          <div>
            <!-- Engine Displacement Present only for GStack region sites -->
          </div>

          <!---->

          <!----><div ng-if="(lotDetails.ft | trim)!='' || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <label data-uname="lotdetailFuel" class="bold">
                Fuel:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailFuelvalue">
                GAS
              </span>
            </div>
          </div><!---->

          <!----><div ng-if="(lotDetails.hk | trim)!='' || !hideEmptyFields">
            <div class="pt-8 d-flex border-top-gray">
              <!--Keys-->
              <label for="Keys:" data-uname="lotdetailKey" class="bold">
                Keys:
              </label>
              <span class="lot-details-desc" data-uname="lotdetailKeyvalue">
                YES
              </span>
            </div>
          </div><!---->

          <div>
            <!-- Present only for UK region sites -->
          </div>

          <!---->
          <!---->

          <div><!--Interior Type--></div>

          <div><!--Navigation--></div>

          <div><!--Navigation Disk--></div>

          <div><!--Owners Manual--></div>

          <div>
            <!-- Document Present only for GStack region sites -->
          </div>

          <div>
            <!-- Gross Weight Present only for GStack region sites -->
          </div>

          <div>
            <!-- Additional Info Present only for GStack region sites -->
          </div>

          <div>
            <!-- Download PDF Present only for GStack region sites -->
          </div>

          <div>
            <!-- Buildsheet Present only for GStack region sites -->
          </div>

          

          <div></div>

          <!---->

          <!---->

          <!----><div ng-if="iconCodesObjArray &amp;&amp; iconCodesObjArray.length &amp;&amp; !showCopartSelectCode">
            <div class="pt-8 d-flex border-top-gray d-flex">
              <!--Highlights-->
              <label for="Highlights:" class="lot-veh-icon bold" data-uname="lotdetailHighlights">
                Highlights:
              </label>
              <div class="w100">
                <!----><span class="lot-details-desc highlights-popover-cntnt text-CERT-E d-flex j-c_s-b" fragment-id="CERT-E" ng-repeat="iconObj in iconCodesObjArray">
                  <span>
                    <!---->
                    Enhanced Vehicles</span>
                  <!----><a ng-if="iconObj.iconCode &amp;&amp; iconObj.iconCode.indexOf('CERT-D') == -1" class="icon-tooltip" data-trigger="focus" data-toggle="popover" fragment-id="CERT-E" data-placement="auto right" data-html="true" data-uname="lotdetailHighlightstooltip">
                    <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
                  </a><!---->
                </span><!---->
              </div>
            </div>
          </div><!---->
          <div>
            <!---->
          </div>

          <div>
            <!---->
          </div>

          <div>
            <!----><div ng-if="!showCopartSelectCode" class="pt-8 d-flex border-top-gray d-f flex-wrap" ng-class="(lotDetails.sn || lotDetails.ltnte) ? '':''">
              <label for="Notes:" data-uname="lotdetailNotes" class="bold">
                Notes:
              </label>
              <div ng-switch="" on="!!lotDetails.sn || !!lotDetails.ltnte || !!isEligibleForCarFaxNote">
                <!---->
                <!----><div ng-switch-default="">
                  <div class="lot-details-desc clr lot-detail-notes-empty f-g1" data-uname="lotdetailNotesvalue">
                    There are no Notes for this Lot
                  </div>
                </div><!---->
              </div>
            </div><!---->
          </div>
        </div>


"""













from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

details = {}

# Iterate over each label and corresponding value
for label_elem in soup.select('div.f-g2 label'):
    label = label_elem.text.strip()
    label = label.replace(":", "")
    
    # Find the corresponding value
    value_elem = label_elem.find_next(class_='lot-details-desc')
    value = value_elem.text.strip() if value_elem else None
    value = value.replace("\n", "").replace("  ", "")
    
    # Add the key-value pair to the details dictionary
    details[label] = value

# Print the scraped details
for key, value in details.items():
    print(f"{key}: {value}")

import json
print(json.dumps(details))


print("\n\n\n")






















html_content = """

<div class="bid-info-content" ng-if="!isUpcomingLot">
            <div class="row lot-details-content">
                <div class="col-md-12 col-xs-12">
                    <!---->

                    <!----><div class="lot-details-inner" ng-if="dynamiclotDetails !== undefined">
                        <!---->

                        <!----><div ng-if="dynamiclotDetails.lotAuctionStatus != 'COUNTER_BIDDING' &amp;&amp; !dynamiclotDetails.sealedBid">
                            <!--  Prelimbidding and live bid comes here -->
                            <!---->
                            <!----><div ng-if="dynamiclotDetails.lotAuctionStatus != 'LIVE_BIDDING'">
                                <div>
	<div>
		
		
		
		<div><div tool-tip-pop-over="">
	<form name="prelimBidForm" class="panel-content prelim_bid_form ng-pristine ng-valid ng-valid-maxlength">
		<!-- Bid Status -->
		<div class="d-flex" ng-switch="" on="dynamiclotDetails.bidStatus">
			<label for="Bid Status">
				Bid Status:
			</label>
			<span>
        <!-- OutBid -->
        <!---->
				<!-- Winning -->
        <!---->
				<!-- Other than winning or outbid,dynamically populate the status -->
        <!----><span ng-switch-default="" class="lot-details-desc ng-hide" ng-show="!isAnonymous">
          You Haven't Bid
        </span><!---->
      </span>
		</div>

		<!--Check Bid Eligibility-->
		<div class="bid-eligibility border-top-gray">
			
    <div class="pt-5 d-flex">
        <label>Eligibility Status:</label>
        <span>
      <!--for guest user-->
      <span class="check-now lot-details-desc" ng-click="checkBidEligibility();" ng-show="!eligibilityChecked &amp;&amp; !(buyerStatus == 'I' || buyerStatus == 'P')">
        <img src="../images/lot-details/lot-details-sprite.svg" alt="Check Now" class="img-responsive yellow-circle mr-5">
        <a class="bl-link" check-for-logged-in-user="">
          Check Now
          <i class="fa fa-angle-right"></i>
        </a>
      </span>
            <!--for eligible user-->
      <span class="eligible ng-hide" ng-show="eligibleToBid">
        <span class="font-green">
          <img src="../images/lot-details/lot-details-sprite.svg" class="img-responsive green-circle">
          Eligible to Bid.
        </span>
      </span>
            <!--for non-eligible user-->
      <span class="not-eligible ng-hide" ng-show="notEligibleBid || (buyerStatus == 'I' || buyerStatus == 'P')">
        <span class="font-red">
          <img src="../images/lot-details/lot-details-sprite.svg" class="img-responsive red-circle">
          Not Eligible to Bid.
        </span>
        <a ng-click="checkWhyNotEligible()" class="bold">
          Check Why?
        </a>
      </span>
    </span>
    </div>

		</div>

		<!-- Sale Status -->
		<div class="border-top-gray pt-5 d-flex">
			<label for="Sale Status">
				Sale Status:
			</label>
			<span class="lot-details-desc">
        Minimum Bid
        <a class="icon-tooltip" fragment-id="MINIMUM_BID" data-placement="auto right" data-html="true" data-trigger="focus" data-toggle="popover" data-uname="lotDetailSaleStatusTooltip">
          <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
        </a>
      </span>
		</div>

		<!----><div class="border-top-gray pt-5 d-flex" ng-if="displayTimeLeftForSale !== undefined">
			<label for="time-left" data-uname="lotdetailSaleinformationtimeleftlabel">
				Time Left:
			</label>

			<span class="d-flex w100">
        <span class="font-red mr-10 bid-time-left" data-uname="lotdetailSaleinformationtimeleftvalue">
          0D 18H 37min
        </span>
        <!----><a ng-if="showAddToCalendar !== undefined" ng-href="/public/data/lot/addToOutlook/2024-02-01T07:00/2024-02-01T07:30/2016 BMW X6 XDRIVE50I/www.copart.com/" target="_blank" class="add-to-calendar" name="addToCalendar" id="addToCalendar-lotinfo" title="Add to Calendar" ng-click="triggerLdpAddToCalendar()" href="/public/data/lot/addToOutlook/2024-02-01T07:00/2024-02-01T07:30/2016 BMW X6 XDRIVE50I/www.copart.com/">
          <i class="lotdetails-icons-redesign addcalendar-icon"></i>
          Add to Calendar</a><!---->
      </span>
		</div><!---->

		

		<!-- If First Bid is Y, then show both starting bid and maximum bid -->
		<!---->

		<!----><div ng-if="!dynamiclotDetails.firstBid">
			<!---->

			<!-- Current Bid -->
			<div class="border-top-gray pt-5 d-flex">
				<!----><label for="Current Bid" ng-if="!dynamiclotDetails.startingBidFlag">Current Bid:</label><!---->
				<!---->
          <span class="bid-price">
            $13,400.00 USD
          </span>

					<!-- sale status is minimum bid -->
          <!----><span ng-if="dynamiclotDetails.saleStatus == 'MINIMUM_BID'">
            <!----><p ng-if="!dynamiclotDetails.sellerReserveMet">
              <span class="text-muted bold reserve-popover-content d-flex">
                Seller Reserve Not Yet Met
                <a class="seller-reserve-popover" href="javascript:void(0)" data-toggle="popover" data-content="Seller has placed a reserve price on the lot. If the minimum bid is not surpassed during the live auction, Seller has until 6 p.m. (Pacific Time) on the next business day following the day of the auction to accept the bid." ng-attr-title="{{locale.messages['lotdetail.label.sellerReserve.title']}}" tooltip="" data-original-title="" title="Seller Reserve">
                  <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
                </a>
              </span>
            </p><!---->

            <!---->
          </span><!---->
        
			</div>

			<!---->

			<!----><div ng-if="dynamiclotDetails.bidStatus == 'NEVER_BID'">
				<div class="border-top-gray bid_action_block">
					<div class="pt-5 pl-15">
						<label class="mr-10">Your Bid:</label>
						<div class="d-flex mt-5">
              <span>
                <input type="radio" name="bid" ng-model="dynamiclotDetails.jumpCurrentBidFlag" id="max_bid" class="radio_bid_btn ng-pristine ng-untouched ng-valid ng-not-empty" value="N" ng-click="clearMaxBidErrorMsg()">
                <label for="max_bid" class="bid_label">Max Bid</label>
              </span>
							<span class="ml-20">
                <span>
                  <input type="radio" name="bid" ng-model="dynamiclotDetails.jumpCurrentBidFlag" id="monster_bid" class="radio_bid_btn ng-pristine ng-untouched ng-valid ng-not-empty" value="Y" ng-click="clearMaxBidErrorMsg()">
                  <label for="monster_bid" class="bid_label">Monster Bid
                    <a href="javascript:void(0)" data-html="true" data-toggle="popover" data-content="A Monster Bid moves the current bid ahead to a specific amount rather than waiting on the incremental bidding to reach that number. This is a great feature for when you have a specific price in mind for a vehicle." ng-attr-title="Monster Bid" aria-label="Monster Bid" tooltip="" data-original-title="" title="">
                      <i class="lotdetails-icons-redesign exclaimer-rd-icon"></i>
                    </a>
                  </label>
                </span>
              </span>
						</div>
					</div>
					<div class="mb-10">
						<div class="d-f mt-10 a-i_c mb-0 pl-15 w100" ng-class="(maxBidErrorMsg !== undefined) &amp;&amp; (maxBidErrorMsg != null) &amp;&amp; (maxBidErrorMsg != '')? 'validation-error-box' : ''">
              <span class="mr-5 fs14">$</span>
							<input class="input-md form-control bid_amount_input max-monster-bid-field ng-pristine ng-untouched ng-valid ng-empty ng-valid-maxlength" id="your-max-bid" name="maxBid" type="text" aria-label="Your Max Bid" numbers-only="" ng-model="dynamiclotDetails.bidAmount" maxlength="7" autocomplete="off">
						</div>
						<div class="counter-error lightred bold errorstyle ml-30 ng-hide" ng-show="maxBidErrorMsg">
							
						</div>
					</div>
					<div class="d-f ml-30">
            <span class="dynamic-bid-inc clr text-muted fs11">
              ($100.00 USD&nbsp;Bid Increment)
            </span>
						<a ng-click="bidIncrementGuidelinesModal()" class="ml-5 fs11 bl-link guideline-link">
							Incremental Bid Guidelines
						</a>
					</div>
					<!---->
					<!----><div class="d-f j-c_c pt-5 bidnow-button" ng-if="buyerStatus !=='I'">
						<button name="id " class="btn btn-yellow-rd" check-for-logged-in-user="" ng-click="openIncreaseBidModal()" role="button" aria-label="Bid Now">
							Bid Now
							<i class="lotdetails-icons-redesign arrow-right-rd-icon right"></i>
						</button>
					</div><!---->
					<!----><div class="price-estimator-block mx-10" ng-if="showPricingCalculatorPref">
						<!----><pricing-calculator-component [lot-details]="lotDetails" [currency-code]="lotDetails.cuc" [country-code]="lotDetails.locCountry" [title-group-code]="lotDetails.tgc" (bid-amount-change)="populateMaxBid($event)" [bid-amount]="dynamiclotDetails.bidAmount" ng-if="appInit.lazyLoadedModules.lotDetailsApp" _nghost-ctt-c120="" ng-version="14.3.0"><!----><p-dialog _ngcontent-ctt-c120="" styleclass="cprt-dialog price-estimator-dialog" appendto="body" class="p-element ng-tns-c56-0"><!----></p-dialog><!----></pricing-calculator-component><!---->
					</div><!---->
				</div>

				

				<!---->

				<div class="bid_disclaimer_block clr">
    <!----><p class="full-width bid_disclaimer" ng-if="locale.messages['app.label.asIsWhereIsDisclaimer']">
        <span class="gray-text">All bids are legally binding and all sales are final.</span>
        <a class="bl-link disclaimer-learnmore" ng-click="openAsIsModal()">
            Learn More
        </a>
    </p><!---->

    <!---->
</div>
			</div><!---->
		</div><!---->
	</form>
</div></div>
	</div>
</div>
                            </div><!---->
                        </div><!---->

                        <!---->
                    </div><!---->
                </div>
            </div>
        </div>
"""











soup = BeautifulSoup(html_content, 'html.parser')
bid_details = {}
# Extract Sale Status
bid_div_main = soup.find('div', class_="bid-info-content")
all_bid_divs = bid_div_main.find_all('div', class_="border-top-gray") if bid_div_main else []
print("BID INFO")
for bid_div in all_bid_divs:
    label_elem = bid_div.find("label")
    label = label_elem.get_text(strip=True) if label_elem else ""
    label = label.replace(":", "")
    span_ele = bid_div.find("span")
    span = span_ele.get_text(strip = True) if span_ele else ""
    span = span.replace("Add to Calendar", "")
    if label == "Eligibility Status" or label == "Your Bid":
        continue
    bid_details [label] = span
    print(f"{label}: {span}")














html_content= """

<div id="sale-information-block" class="panel clr overflowHidden" tool-tip-pop-over="">
    <div class="panel-heading">
        <h3 data-uname="lotdetailSaleinformationlabel">
            Sale Information
            <hr class="s-h-separator">
        </h3>
    </div>

    <div class="panel-content">
        <div class="d-flex">
            <label for="sale yard name">Sale Name:</label>
            <span class="lot-details-desc">
        <!----><span ng-if="dynamiclotDetails.lotAuctionStatus != 'COUNTER_BIDDING'">
          <a ng-click="getAllLaneSaleListResultUrl(lotDetails)">*NCS - CENTRAL REGION</a>
        </span><!---->
        <!---->
      </span>
        </div>

        <div class="border-top-gray pt-5 d-flex">
            <label for="location" data-uname="lotdetailSaleinformationlocationlabel">
                Sale Location:
            </label>

            <span class="lot-details-desc">
        <a target="_blank" href="/locations/dallas-tx-12" data-uname="lotdetailSaleinformationlocationvalue">TX - DALLAS
        </a>
      </span>
        </div>

        <!---->

        <!--
               If the sale is in future, we just show future
               If not, we display the sale date, sale time and add to calendar
            -->
        <div class="border-top-gray d-flex pt-5">
            <label for="sale date:" data-uname="lotdetailSaleinformationsaledatelabel">
                Sale Date:
            </label>
            <div class="lot-details-desc" ng-switch="" on="lotDetails.ifs &amp;&amp; lotDetails.ifs.toString()">
                <!---->
                <!----><div ng-switch-default="">
                    <!----><p class="bold" ng-if="validateDate(lotDetails.ad)">
            <span data-uname="lotdetailSaleinformationsaledatevalue">
              Thu. Feb 01, 2024<br>
              07:00 AM PKT<br>
            </span>
                    </p><!---->
                    <!---->
                </div><!---->
            </div>
        </div>

        <!---->

        <!---->

        <div class="border-top-gray pt-5 d-flex" pref-code="lotDetailsPreference.showLastUpdateDate" access-value="true">
            <label for="last-updated" data-uname="lotdetailSaleinformationlastUpdatedlabel">
                Last Updated:
            </label>
            <span class="lot-details-desc" data-uname="lotdetailSaleinformationlastupdatedvalue">
        01/30/2024 1:03 am
      </span>
        </div>

        <!---->

        <!---->
    </div>
</div>

""" 


print("\n\n\n")




soup = BeautifulSoup(html_content, 'html.parser')

# Extract Sale Information
sale_info_div = soup.find('div', {'id': 'sale-information-block'})
sale_info_label = sale_info_div.find('h3').get_text(strip=True)
print(f"{sale_info_label}:")
print('-' * len(sale_info_label))  # Adding separator

# Extract key-value pairs dynamically
info_pairs = sale_info_div.find_all('div', class_='d-flex')
for pair in info_pairs:
    label = pair.find('label').get_text(strip=True)
    value = pair.find('span').get_text(strip=True)
    print(f"{label}: {value}")








  # vehicle_details = {
    #     "Lot Number": "",
    #     "VIN": "",
    #     "Title Code": "",
    #     "Odometer": "",
    #     "Primary Damage":"",
    #     "Cylinders": "",
    #     "Body Style": "",
    #     "Color": "",
    #     "Engine Type": "",
    #     "Transmission": "",
    #     "Drive": "",
    #     "Vehicle Type": "",
    #     "Fuel": "",
    #     "Keys": "",
    #     "Highlights": "",
    #     "Notes": ""
    # }
    # bid_information = {
    #     "Sale Status": "",
    #     "Time Left": "",
    #     "Current Bid": "",
    # }
    # sale_information= {
    #     "Sale Name": "",
    #     "Sale Location": "",
    #     "Sale Date" : "",
    #     "Last Updated" : ""
    # }




html = """

<div class="small-container martop">
            <div id="small-img-roll" class="d-flex thumbImgContainer thumb-scroll" ng-class="(thumbNailImages.length>10) ? 'thumb-scroll':''">
                <!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/f3031d5e0f134bb396ea5ac047b4ea2d_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/f3031d5e0f134bb396ea5ac047b4ea2d_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/f3031d5e0f134bb396ea5ac047b4ea2d_hrs.jpg" target-index="0" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/f3031d5e0f134bb396ea5ac047b4ea2d_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3c178bc24422469e833038bca6310244_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3c178bc24422469e833038bca6310244_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3c178bc24422469e833038bca6310244_hrs.jpg" target-index="1" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3c178bc24422469e833038bca6310244_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/c26ff067d0e64423b83ad2b5d1e5146d_thb.jpg" class="img-responsive cursor-pointer thumbnailImg active" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/c26ff067d0e64423b83ad2b5d1e5146d_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/c26ff067d0e64423b83ad2b5d1e5146d_hrs.jpg" target-index="2" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/c26ff067d0e64423b83ad2b5d1e5146d_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/67cfccd085bc4c11b25e70e8e2e05168_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/67cfccd085bc4c11b25e70e8e2e05168_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/67cfccd085bc4c11b25e70e8e2e05168_hrs.jpg" target-index="3" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/67cfccd085bc4c11b25e70e8e2e05168_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/09980858c63e498aa84a75efb1d7ef3e_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/09980858c63e498aa84a75efb1d7ef3e_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/09980858c63e498aa84a75efb1d7ef3e_hrs.jpg" target-index="4" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/09980858c63e498aa84a75efb1d7ef3e_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/db729320972f4064ac5a47397b32b442_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/db729320972f4064ac5a47397b32b442_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/db729320972f4064ac5a47397b32b442_hrs.jpg" target-index="5" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/db729320972f4064ac5a47397b32b442_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3606911b0af14fecbbe54e46212bb51d_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3606911b0af14fecbbe54e46212bb51d_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3606911b0af14fecbbe54e46212bb51d_hrs.jpg" target-index="6" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/3606911b0af14fecbbe54e46212bb51d_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/221bc7e7ad394fd4a7fef9f36228a8f9_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/221bc7e7ad394fd4a7fef9f36228a8f9_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/221bc7e7ad394fd4a7fef9f36228a8f9_hrs.jpg" target-index="7" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/221bc7e7ad394fd4a7fef9f36228a8f9_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/2d5402524fad47958aa214ad7999f585_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/2d5402524fad47958aa214ad7999f585_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/2d5402524fad47958aa214ad7999f585_hrs.jpg" target-index="8" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/2d5402524fad47958aa214ad7999f585_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/d45a68ce0ffc46629938647450851fe2_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/d45a68ce0ffc46629938647450851fe2_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/d45a68ce0ffc46629938647450851fe2_hrs.jpg" target-index="9" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/d45a68ce0ffc46629938647450851fe2_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/a667ce6026b240abb447143a864b0e0b_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/a667ce6026b240abb447143a864b0e0b_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/a667ce6026b240abb447143a864b0e0b_hrs.jpg" target-index="10" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/a667ce6026b240abb447143a864b0e0b_thb.jpg">
                </span><!----><span ng-repeat="image in thumbNailImages" class="thumbImgblock" on-finish-render="ngRepeatFinished">
                <img ng-src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/1783ce70b21b4cd1b2e85f33b79a92f6_thb.jpg" class="img-responsive cursor-pointer thumbnailImg" error-image="" title="2016 BMW X6 XDRIVE50I" alt="2016 BMW X6 XDRIVE50I for Sale at Copart TX - DALLAS" full-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/1783ce70b21b4cd1b2e85f33b79a92f6_ful.jpg" hd-url="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/1783ce70b21b4cd1b2e85f33b79a92f6_hrs.jpg" target-index="11" ng-click="showImg($index,false)" src="https://cs.copart.com/v1/AUTH_svc.pdoc00001/lpp/0124/1783ce70b21b4cd1b2e85f33b79a92f6_thb.jpg">
                </span><!---->
            </div>
        </div>

"""



soup = BeautifulSoup(html, 'html.parser')

# Extract image URLs
image_urls = []

thumb_img_blocks = soup.find_all('span', class_='thumbImgblock')
for thumb_img_block in thumb_img_blocks:
    img_url = thumb_img_block.find('img', class_='thumbnailImg')['ng-src']
    # Replace the ng-src attribute with the actual image URL
    img_url = img_url.replace('{{$index}}', '0')
    img_url = img_url.replace("thb", "ful")
    image_urls.append(img_url)

# Print the list of image URLs
for index, img_url in enumerate(image_urls, start=1):
    print(f"Image {index}: {img_url}")