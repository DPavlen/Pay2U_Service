import { ReactElement, useEffect } from 'react';
import './PurchasePage.scss';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import ServiceHeader from '../../components/ServiceHeader/ServiceHeader.tsx';
import {
  IPurchseShippingFields,
  ITariff,
} from '../../utils/interfaces/interfaces.ts';
import { SubmitHandler, useForm, Controller } from 'react-hook-form';
import {
  Button,
  Checkbox,
  FormControlLabel,
  FormGroup,
  Radio,
  RadioGroup,
} from '@mui/material';
import { SwitchLovely } from '../../components/uxComponents/switch.ts';
import { useDispatchTyped, useSelectorTyped } from '../../hooks/store.ts';
import styled from 'styled-components';
import api from '../../utils/api/Api.ts';
import { addPaymentHistory, addUserSubscriptions } from '../../services/currentUserSlice.ts';

const Form = styled.form`
  padding-bottom: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: calc(100svh - 72px);
`;

const MainWrapper = styled.div`
  width: 100%;
  flex: 1 0 auto;
`;

const StyledServiceHeader = styled(ServiceHeader)`
  padding-block: 20px 8px;
`;

const SectionTitle = styled.h2`
  margin: 0;
  padding-bottom: 16px;
  font-size: 20px;
  font-weight: 600;
`;

const SmallText = styled.span`
  margin: 0;
  font-size: 12px;
  font-weight: 400;
`;

const AcceptSmallText = styled.span`
  font-size: 14px;
  font-weight: 600;
`;

const RadioButton = styled(FormControlLabel)`
  && {
    margin: 0;
    padding-inline: 12px;
    justify-content: space-between;
    & img {
      height: 39px;
    }
    & .MuiTypography-root {
      display: flex;
      align-items: center;
      gap: 12px;
    }
  }
`;

const AutopaymentSwitch = styled(FormControlLabel)`
  && {
    margin: 0;
    padding-block: 20px 24px;
    gap: 12px;
    justify-content: flex-end;
    & input {
      width: auto;
    }
  }
`;

const StyledCheckbox = styled(FormControlLabel)`
  & .MuiFormControlLabel-label {
    font-size: 12px;
  }

  & a {
    color: var(--navy-blue-2);
  }
`;

function PurchasePage(): ReactElement {
  const dispatch = useDispatchTyped();
  const navigate = useNavigate();
  const paymentMethods = useSelectorTyped(
    (store) => store.currentUserReducer.paymentMethods
  );
  const reversedPaymentMethods = [...paymentMethods].reverse();
  const subscription = useLocation().state.subscription;
  const tariff: ITariff = useLocation().state.selectTariff;
  const {
    control,
    handleSubmit,
    setValue,
    formState: { isValid, isDirty },
  } = useForm<IPurchseShippingFields>({
    defaultValues: {
      subscriptionId: subscription.id,
      autopayment: true,
      paymentMethodId: 1,
      terms: false,
      politics: false,
    },
    mode: 'onTouched',
  });

  useEffect(() => {
    const foundPaymentMethod = paymentMethods.find(
      (item) => item.payment_method === 'СБП'
    );
    if (foundPaymentMethod) {
      setValue('paymentMethodId', foundPaymentMethod.id);
    }
  }, [paymentMethods, setValue]);

  function calculatePrice() {
    if (tariff.tariff_promo_price || tariff.tariff_promo_price !== null) {
      if (tariff.services_duration === '1') {
        return (
          <AcceptSmallText>
            {tariff.tariff_promo_price / Number(tariff.services_duration)} ₽{' '}
            <SmallText>за месяц, далее {tariff.tariff_full_price} ₽</SmallText>
          </AcceptSmallText>
        );
      } else {
        return (
          <AcceptSmallText>
            {Math.trunc(
              tariff.tariff_promo_price / Number(tariff.services_duration)
            )}{' '}
            ₽ <SmallText>за месяц</SmallText>
          </AcceptSmallText>
        );
      }
    } else {
      return (
        <AcceptSmallText>
          {Math.trunc(
            tariff.tariff_full_price / Number(tariff.services_duration)
          )}{' '}
          ₽ <SmallText>за месяц</SmallText>
        </AcceptSmallText>
      );
    }
  }

  const onSubmit: SubmitHandler<IPurchseShippingFields> = (data) => {
    data.tariffId = tariff.id;
    data.paymentMethodId = Number(data.paymentMethodId);
    api
      .purchase(data)
      .then((res) => {
        Promise.all([api.getUserSubscriptions(), api.getPaymentHistory()])
          .then((res) => {
            dispatch(addUserSubscriptions(res[0]));
            dispatch(addPaymentHistory(res[1]));
          })
          .catch(console.error);
        navigate('/successful-purchase', {
          state: { data: res },
          replace: true,
        });
      })
      .catch(console.error);
  };

  return (
    <section className="purchase-page">
      <Form className="purchase-page__form" onSubmit={handleSubmit(onSubmit)}>
        <MainWrapper>
          <StyledServiceHeader selectSubscription={subscription} />
          <div className="purchase-page__tariff-title-wrap">
            <h2>{tariff.name}</h2>
          </div>
          {calculatePrice()}
          <p className="purchase-page__total">
            <span>Итого:</span>
            <span>
              {tariff.tariff_promo_price || tariff.tariff_full_price} ₽
            </span>
          </p>
          <SectionTitle>Способ оплаты</SectionTitle>
          <Controller
            control={control}
            name="paymentMethodId"
            render={({ field }) => (
              <RadioGroup name="paymentMethodId" value={field.value}>
                {reversedPaymentMethods.map((method, index) => (
                  <RadioButton
                    label={
                      <>
                        <img src={method.icon} alt={method.methodName} />
                        <SmallText>{method.payment_method}</SmallText>
                      </>
                    }
                    labelPlacement="start"
                    key={`payment-method-${index}`}
                    control={<Radio />}
                    onChange={(e) => field.onChange(e)}
                    value={method.id}
                  />
                ))}
              </RadioGroup>
            )}
          />
          <Controller
            control={control}
            name="autopayment"
            render={({ field }) => (
              <AutopaymentSwitch
                checked={field.value}
                control={<SwitchLovely color="primary" />}
                label="Подключить автоплатеж"
                labelPlacement="start"
                onChange={(e) => field.onChange(e)}
                value={field.value}
              />
            )}
          />
          <FormGroup>
            <Controller
              control={control}
              name="terms"
              rules={{ required: true }}
              render={({ field }) => (
                <StyledCheckbox
                  checked={field.value}
                  value={field.value}
                  required
                  onChange={(e) => field.onChange(e)}
                  control={<Checkbox />}
                  label={
                    <>
                      <span>Принимаю</span>{' '}
                      <Link to={'404'}>условия сервиса</Link>
                    </>
                  }
                />
              )}
            />
            <Controller
              control={control}
              name="politics"
              rules={{ required: true }}
              render={({ field }) => (
                <StyledCheckbox
                  checked={field.value}
                  value={field.value}
                  required
                  onChange={(e) => field.onChange(e)}
                  control={<Checkbox />}
                  label={
                    <>
                      <span>Принимаю</span>{' '}
                      <Link to={'404'}>политику обработки данных</Link>
                    </>
                  }
                />
              )}
            />
          </FormGroup>
        </MainWrapper>
        <Button
          disabled={!isDirty || !isValid}
          type="submit"
          variant="contained"
        >
          Оплатить
        </Button>
      </Form>
    </section>
  );
}

export default PurchasePage;
