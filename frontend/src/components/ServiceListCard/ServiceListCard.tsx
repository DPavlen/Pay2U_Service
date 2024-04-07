import { ReactElement } from 'react';
import { Link } from 'react-router-dom';
import { IServiceExtended } from '../../utils/interfaces/interfaces';
import styled from 'styled-components';

interface IServiceListCardProps {
  service: IServiceExtended;
}

const CardLink = styled(Link)`
  border-radius: 12px;
  padding: 16px;
  max-height: 74px;
  box-sizing: border-box;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 16px;
  text-decoration: none;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.05);

  & img {
    display: block;
    max-height: 40px;
    border-radius: 50px;
  }

  & h3 {
    margin: 0;
    font-size: 15px;
    font-weight: 500;
    line-height: 1.2;
    color: var(--black);
  }
  & p {
    margin: 0;
    font-size: 14px;
    font-weight: 600;
    line-height: 1.43;
    color: var(--grey-1);
  }
`;

const DescrtiptionWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 4px;
`;

export default function ServiceListCard(
  props: IServiceListCardProps
): ReactElement {
  const lowestPrice = Math.min(
    ...props.service.tariff.map((t) => t.tariff_promo_price)
  );

  return (
    <li>
      <CardLink to={`/services/${props.service.id}`}>
        <img src={props.service.icon_small} alt="" />
        <DescrtiptionWrapper>
          <h3>{props.service.name}</h3>
          <p>
            {lowestPrice === Infinity ? (
              <span>Недоступен для подписки &#128546;</span>
            ) : (
              `От ${lowestPrice} ₽ в месяц`
            )}
          </p>
        </DescrtiptionWrapper>
      </CardLink>
    </li>
  );
}
